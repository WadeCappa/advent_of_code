from functools import reduce
from collections import defaultdict
import sys

def getScore(grid, p):
    if grid[p] == sys.maxsize:
        return 0
    v = 0
    if grid[p] == 9:
        v += 1
    for dy, dx in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
        y, x = p
        if grid[(y + dy, x + dx)] == grid[p] + 1:
            v += getScore(grid, (y + dy, x + dx))
    return v

if __name__ == "__main__":
    file = sys.argv[1]
    grid = defaultdict(lambda: sys.maxsize)
    starts = []
    with open(file) as f:
        for j, l in enumerate(f):
            for i, v in enumerate(l.strip()):
                grid[(j, i)] = int(v)
                if v == "0":
                    starts.append((j, i))
    
    print(reduce(lambda acc, x: getScore(grid, x) + acc, starts, 0))