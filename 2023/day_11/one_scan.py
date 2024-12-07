import sys
from solution import loadGraph, getExpandedRowsAndCols

def getPoints(g):
    points = []
    for j, r in enumerate(g):
        for i, v in enumerate(r):
            if v == '#':
                points.append((j, i))
    return points

def getDistance(s, e, rows, cols, co):
    res = 0
    for r in rows:
        if r > s[0] and r < e[0]:
            res += co
    for c in cols:
        if (c > s[1] and c < e[1]) or (c < s[1] and c > e[1]):
            res += co
    res += abs(e[0] - s[0])
    res += abs(e[1] - s[1])
    return res

def sumDistances(p, points, rows, cols, co):
    res = 0
    for e in points:
        res += getDistance(p, e, rows, cols, co)
    return res

if __name__ == "__main__":
    file = sys.argv[1]
    co = int(sys.argv[2])
    g = loadGraph(file)
    points = getPoints(g)
    rows, cols = getExpandedRowsAndCols(g)
    print(rows, cols)
    
    res = 0
    seen = set()
    for s in points:
        for e in points:
            if (s, e) not in seen and (e, s) not in seen:
                seen.add((s, e))
                seen.add((e, s))
                d = getDistance(s, e, rows, cols, co)
                res += d
    print(res)
        # res += sumDistances(p, points[i:], rows, cols, co)