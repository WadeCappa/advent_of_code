import sys

xmas = "XMAS"

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
        for i, _ in enumerate(r):
            for dy in [0, 1, -1]:
                for dx in [0, 1, -1]:
                    if dy == 0 and dx == 0:
                        continue
                    print(j, i, dy, dx)
                    res += findxmas((j, i), (dy, dx), 0, grid)
    print(res)