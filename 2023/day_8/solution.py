import sys
import math
from functools import reduce

class Instructions:
    def __init__(self, moves):
        self.moves = moves

    def __iter__(self):
        self.p = 0
        return self

    def __next__(self):
        i = self.moves[self.p]
        self.p = (self.p + 1) % (len(self.moves) - 1)
        return i

class Node:
    def __init__(self, name, left, right):
        self.name = name
        self.left = left 
        self.right = right
    
    def move(self, lr):
        if lr == 'R':
            return self.right 
        if lr == 'L':
            return self.left
        else:
            print("bad input")

def getInstructions(line):
    return Instructions(line)

def buildNode(line):
    name, lr = line.split(" = ")
    l, r = lr.replace('\n', '').replace('(', '').replace(')', '').replace(' ', '').split(",")
    return Node(name, l, r)

def distanceToStopNodes(nodes, start, instructions):
    stopDistances = {}
    moves = iter(instructions)
    distance = 0
    node = start
    seen = set()
    while True:
        distance += 1
        m = next(moves)
        node = nodes[node].move(m)
        if (moves.p, node) in seen:
            print("in loop, stopping")
            return stopDistances
        seen.add((moves.p, node))
        if node[-1] == 'Z':
            print("found stop")
            if node not in stopDistances:
                stopDistances[node] = distance
            else:
                print("encountered a duplicate stop. This is likely an error")

def greatestElement(v, values):
    for va in values:
        if v < va:
            return False
    return True

if __name__ == "__main__":
    input = sys.argv[1]
    instructions = None
    with open(input) as f:
        nodes = {}
        for i, l in enumerate(f):
            if i == 0:
                instructions = getInstructions(l)
                continue
            node = buildNode(l)
            nodes[node.name] = node
    
    currentNodes = [x for x in nodes.keys() if 'A' == x[-1]]
    stopNodes = [x for x in nodes.keys() if 'Z' == x[-1]]
    traversals = [distanceToStopNodes(nodes, x, instructions) for x in currentNodes]
    print(currentNodes)
    print(traversals)

    allValues = []
    for t in traversals:
        for _, v in t.items():
            allValues.append(v)
    print(allValues)

    print(math.lcm(traversals))