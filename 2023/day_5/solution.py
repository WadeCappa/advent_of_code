import sys
from collections import deque
from functools import reduce, cache


class Table:
    def __init__(self, ranges, name):
        self.ranges = ranges
        self.name = name

    def traverse(self, input):
        for r in self.ranges:
            if r.inRange(input):
                return r.traverse(input)
        return input
    
class Range:
    def __init__(self, source, destination, size):
        self.source = source 
        self.destination = destination
        self.size = size

    def inRange(self, input):
        return input >= self.source and input - self.source <= self.size
    
    def rangeInRange(self, start, end):
        if self.inputOnLeft(start):
            if self.inputOnRight(end) or self.inRange(end):
                return True
            else: 
                return False
        elif self.inRange(start):
            if self.inputOnRight(end) or self.inRange(end):
                return True
            else:
                print(f"start: {start}, end {end}, self.source {self.source}, self.end {self.source + self.size}")
                return False
        else:
            return False 

    def inputOnLeft(self, input):
        return self.source > input
    
    def inputOnRight(self, input):
        return self.source + self.size < input
    
    def getEndOfRange(self):
        return self.source + self.size
    
    def traverse(self, input):
        diff = input - self.source
        return self.destination + diff

    def traverseRange(self, newRangeStart, newRangeEnd):
        defaultCase = [(newRangeStart, newRangeEnd, False)]
        if self.inputOnLeft(newRangeStart):
            if self.inputOnRight(newRangeEnd):
                return [(newRangeStart, self.source - 1, False), (self.destination, self.destination + self.size, True), (self.source + self.size + 1, newRangeEnd, False)]
            elif self.inRange(newRangeEnd):
                return [(newRangeStart, self.source - 1, False), (self.destination, self.traverse(newRangeEnd), True)]
            else: 
                return defaultCase
        elif self.inRange(newRangeStart):
            if self.inputOnRight(newRangeEnd):
                return [(self.traverse(newRangeStart), self.traverse(self.getEndOfRange()), True), (self.getEndOfRange() + 1, newRangeEnd, False)]
            elif self.inRange(newRangeEnd):
                return [(self.traverse(newRangeStart), self.traverse(newRangeEnd), True)]
            else:
                print("should not be possible, this should throw")
                return defaultCase
        else:
            return defaultCase

def asRanges(tokens):
    res = []
    for token in tokens:
        values = [int(x) for x in token.split()]
        res.append(Range(values[1], values[0], values[2]))
    return res

def getTables(tokens):
    res = []
    for line in tokens:
        tokens = line.split("\n")
        name = tokens[0].split()[0]
        res.append(Table(asRanges(tokens[1:]), name))
    return res

def getMinimalSeed(tables, seeds):
    result = sys.maxsize
    for s in seeds:
        value = s
        for t in tables:
            value = t.traverse(value)
        result = min(result, value)
    return result

def traversalWithRanges(tables, ranges):
    bfs = deque()
    best = sys.maxsize
    for s, e in ranges:
        bfs.append((s, e, 0))
    while bfs:
        s, e, l = bfs.popleft()
        if l == len(tables):
            best = min(best, s)
            continue
        passedRange = False
        for r in tables[l].ranges:
            if r.rangeInRange(s, e):
                passedRange = True
                newRanges = r.traverseRange(s, e)
                while newRanges:
                    nS, nE, d = newRanges.pop()
                    bfs.append((nS, nE, l + 1 if d else l))
        if not passedRange:
            bfs.append((s, e, l + 1))
    return best

def getSeedsAsRanges(seeds):
    res = []
    for i in range(len(seeds) // 2):
        start = seeds[i*2]
        end = seeds[i*2 + 1]
        res.append((start, start + end))
    return res

if __name__ == "__main__":
    input = sys.argv[1]
    tables = None
    with open(input) as f:
        data = f.read()
        tokens = data.split("\n\n")
        seeds = [int(x) for x in tokens[0].split(":")[1].split()]
        print(seeds)
        tables = getTables(tokens[1:])
    
    seedsAsRanges = getSeedsAsRanges(seeds)
    print(traversalWithRanges(tables, seedsAsRanges))