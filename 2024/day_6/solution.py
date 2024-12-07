from collections import defaultdict
import sys

sys.setrecursionlimit(15000)

def getDirections():
    while True:
        yield (-1, 0)
        yield (0, 1)
        yield (1, 0)
        yield (0, -1)

def intoGrid(grid, j):
    p = (-1, -1)
    for i, c in enumerate(l.strip()):
        grid[(j, i)] = c
        if c == '^':
            p = (j, i)
    return p

def checkIfLoop(grid, start):
    seen = set()
    d = getDirections()

    def dfs(j, i, dy, dx):
        if grid[(j, i)] == "X":
            return False
        if (j, i, dy, dx) in seen:
            return True
        seen.add((j, i, dy, dx))
        ny, nx = j + dy, i + dx
        while grid[(ny, nx)] == "#":
            dy, dx = next(d)
            ny, nx = j + dy, i + dx
        return dfs(ny, nx, dy, dx)

    x = next(d)
    return dfs(start[0], start[1], x[0], x[1])

def followPath(grid, start):
    seen = set()
    d = getDirections()

    def dfs(j, i, dy, dx):
        if grid[(j, i)] == "X":
            return

        seen.add((j, i))
        ny, nx = j + dy, i + dx
        while grid[(ny, nx)] == "#":
            dy, dx = next(d)
            ny, nx = j + dy, i + dx
        dfs(ny, nx, dy, dx)

    x = next(d)
    dfs(start[0], start[1], x[0], x[1])
    return seen
    
if __name__ == "__main__":
    file = sys.argv[1]
    grid = defaultdict(lambda:"X")
    s = (-1, -1)
    with open(file) as f:
        for j, l in enumerate(f):
            p = intoGrid(grid, j)
            if p != (-1, -1):
                s = p

    res = 0
    path = followPath(grid, s)
    print(f"path of length {len(path)}")
    for p in path:
        prev = grid[p]
        grid[p] = "#"
        if checkIfLoop(grid, s):
            res += 1
        grid[p] = prev
    print(res)