from functools import reduce
import sys

xmas = "MAS"

def checkValue(j, i, grid, v):
    if j < 0 or j >= len(grid) or i < 0 or i >= len(grid[j]):
        return False
    return grid[j][i] == v

def checkIfCross(points, grid):
    w_i = 0
    for j, i in points:
        if not checkValue(j, i, grid, xmas[w_i]):
            return False
        w_i += 1
    return True

def findxmas(p, d, x_i, grid):
    j, i = p
    if x_i == len(xmas):
        return 1
    if j < 0 or j >= len(grid) or i < 0 or i >= len(grid[j]):
        return 0
    if grid[j][i] != xmas[x_i]:
        return 0
    dy, dx = d
    return findxmas((j + dy, i + dx), d, x_i + 1, grid)

if __name__ == "__main__":
    file = sys.argv[1]
    grid = []
    with open(file) as f:
        grid = [l.strip() for l in f]
    print(grid)

    res = 0
    for j, r in enumerate(grid):
        for i, v in enumerate(r):
            if v != 'A':
                continue
            vals = []
            for dy in [1, -1]:
                for dx in [1, -1]:
                    print(dy, dx)
                    vals.append(checkIfCross([(j - dy, i - dx), (j, i), (j + dy, i + dx)], grid))
            t = 0
            for v in vals:
                if v:
                    t += 1
            print(vals, t)
            if t == 2:
                res += 1
    print(res)