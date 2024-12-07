import sys
from collections import deque
from functools import reduce

def loadGraph(file):
    with open(file) as f:
        return [l[:-1] for l in f]

def getExpandedRowsAndCols(g):
    rows = [i for i, r in enumerate(g) if '#' not in r]
    print(rows)
    cols = []
    for i in range(len(g[0])):
        hasGalaxy = False
        for j in range(len(g)):
            if g[j][i] == '#':
                hasGalaxy = True
                break
        if not hasGalaxy:
            cols.append(i)
    print(cols)
    print(g)
    return (rows, cols)

def withExpansion(j, i, rows, cols, co):
    y, x = j, i
    for r in rows:
        if r < j:
            y += co
    for c in cols:
        if c < i:
            x += co
    return (y, x)

def getPoints(g, rows, cols, co):
    points = []
    for j, r in enumerate(g):
        for i, v in enumerate(r):
            if v == '#':
                points.append(withExpansion(j, i, rows, cols, co))
    return points

def sumShortestPathForPoint(g, p, points, expandedRows, expandedCols, co):
    res = {}
    seen = set()
    bfs = deque([(p[0], p[1], 0)])
    while bfs:
        j, i, d = bfs.popleft()
        if (j,i) in seen or j >= len(g) + co or j < 0 or i >= len(g[0]) + co or i < 0:
            continue
        if (j,i) in points:
            if (j, i) not in res:
                res[(j,i)] = d
            print(f"shortest path for {p} to {(j, i)} is {d}")
            res[(j,i)] = min(res[(j,i)], d)
        seen.add((j, i))
        for dy, di in [(j + 1, i), (j, i + 1), (j - 1, i), (j, i -1)]:
            nextDistance = d + 1
            if dy in expandedRows:
                nextDistance += co
                dy += co
            if di in expandedCols:
                nextDistance += co
                di += co
            bfs.append((dy, di, nextDistance))
    print(res)
    return reduce(lambda x, y: x + y, res.values(), 0)

def sumShortestPaths(g, points, expandedRows, expandedCols, co):
    res = 0
    for i, p in enumerate(points):
        res += sumShortestPathForPoint(g, p, points[i:], expandedRows, expandedCols, co)
    return res

if __name__ == "__main__":
    input = sys.argv[1]
    expansionSize = int(sys.argv[2])
    g = loadGraph(input)
    rows, cols = getExpandedRowsAndCols(g)
    points = getPoints(g, rows, cols, expansionSize)
    print(points)
    print(sumShortestPaths(g, points, rows, cols, expansionSize))