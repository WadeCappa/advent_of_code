import sys
from collections import defaultdict

def getRecords(content):
    return [[int(x) for x in l.split(",")] for l in content.split("\n")]

def getEdges(content):
    edges = defaultdict(set)
    for e in content.split("\n"):
        f, n = e.split("|")
        f, n = int(f), int(n)
        edges[f].add(n)
    return edges

def isSafe(record, edges):
    seen = set()
    for n in record:
        for e in edges[n]:
            if e in seen:
                return False
        seen.add(n)
    return True

def fixRecord(record, edges):
    res = []

    def dfs(n):
        for e in edges[n]:
            if e in record and e not in res:
                dfs(e)
        if n not in res:
            res.append(n)

    for n in record:
        dfs(n)
    return res

if __name__ == "__main__":
    file = sys.argv[1]
    content = ""
    with open(file) as f:
        content = f.read()
    edges, records = content.split("\n\n")
    edges = getEdges(edges)
    records = getRecords(records)
    print(edges)
    print(records)

    res = 0
    for r in records:
        if not isSafe(r, edges):
            fixed = fixRecord(r, edges)
            print(r, fixed)
            res += fixed[len(fixed)//2]
    print(res)