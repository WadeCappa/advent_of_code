import sys
from functools import reduce 

def getSpecialCharsForLine(line):
    res = []
    for i, c in enumerate(line):
        if c != "." and not c.isnumeric():
            res.append(i)
    return res

def calculateSumOfAdjacentNumbers(map, placements):
    numbers = []
    seen = set()
    for i, p in enumerate(placements):
        for j in p:
            for a in [(i + 1, j), (i, j + 1), (i + 1, j + 1), (i - 1, j), (i, j - 1), (i - 1, j - 1), (i + 1, j - 1), (i - 1, j + 1)]:
                if a[0] >= len(map) or a[1] >= len(map[a[0]]):
                    continue
                c = map[a[0]][a[1]]
                if a in seen:
                    continue
                if c.isnumeric():
                    start, end = a[1], a[1]
                    while start >=0 and map[a[0]][start].isnumeric():
                        start -= 1
                    start = max(start, 0)
                    if not map[a[0]][start].isnumeric():
                        start += 1
                    while end < len(map[a[0]]) and map[a[0]][end].isnumeric():
                        end += 1
                    end = min(end, len(map[a[0]])-1)
                    if not map[a[0]][end].isnumeric():
                        end -= 1
                    number = int(map[a[0]][start:end + 1])
                    numbers.append(number)
                    for r in range(start, end + 1):
                        seen.add((a[0], r))
    print(numbers)
    return reduce(lambda x, y: x + y, numbers, 0)

def findAllGears(map, placements):
    res = 0
    gears = set()
    for i, p in enumerate(placements):
        for j in p:
            if map[i][j] != "*":
                continue
            numbers = []
            seen = set()
            for a in [(i + 1, j), (i, j + 1), (i + 1, j + 1), (i - 1, j), (i, j - 1), (i - 1, j - 1), (i + 1, j - 1), (i - 1, j + 1)]:
                if a[0] >= len(map) or a[1] >= len(map[a[0]]):
                    continue
                if a in seen:
                    continue
                c = map[a[0]][a[1]]
                if c.isnumeric():
                    start, end = a[1], a[1]
                    while start >=0 and map[a[0]][start].isnumeric():
                        start -= 1
                    start = max(start, 0)
                    if not map[a[0]][start].isnumeric():
                        start += 1
                    while end < len(map[a[0]]) and map[a[0]][end].isnumeric():
                        end += 1
                    end = min(end, len(map[a[0]])-1)
                    if not map[a[0]][end].isnumeric():
                        end -= 1
                    number = int(map[a[0]][start:end + 1])
                    numbers.append(number)
                    for r in range(start, end + 1):
                        seen.add((a[0], r))
            if len(numbers) == 2:
                res += reduce(lambda x, y: x * y, numbers, 1)
    return res

if __name__ == "__main__":
    input = sys.argv[1]
    map = []
    with open(input) as f:
        map = [x.replace("\n", "") for x in f]
    placements = [getSpecialCharsForLine(l) for l in map] 
    sum = findAllGears(map, placements)
    print(sum)