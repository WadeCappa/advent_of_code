from collections import deque
import sys

def getFixed(nums, forward_edges):
    res = []

    def dfs(n):
        if n not in res and n in nums:
            if n in forward_edges:
                for e in forward_edges[n]:
                    dfs(e)
            if n in nums:
                res.append(n)

    for n in nums:
        dfs(n)
    return res

def isSafe(line, edges):
    placements = {l: i for i, l in enumerate(line)}
    for n, i in placements.items():  
        print(n, edges)
        if n not in edges:
            continue
        for e in edges[n]:
            if e in placements and placements[e] < placements[n]:
                print(f"failed {line}")
                return False
    print(f"passed {line}")
    return True

def getMiddle(nums):
    print(nums)
    return nums[len(nums) // 2]

if __name__ == "__main__":
    file = sys.argv[1]
    data = ""
    with open(file) as f:
        data =f.read()
    paths, lines = data.split("\n\n")
    forward_edges = {}
    reverse_edges = {}
    print(paths)
    for p in paths.split("\n"):
        print(p)
        l, r = p.split("|")
        l, r = int(l), int(r)
        if r not in reverse_edges:
            reverse_edges[r] = []
        if l not in forward_edges:
            forward_edges[l] = []
        reverse_edges[r].append(l)
        forward_edges[l].append(r)
    print(reverse_edges)

    res = 0
    for l in lines.split("\n"):
        print(l)
        nums = [int(x) for x in l.split(",")]
        if not isSafe(nums, forward_edges):
            fixed = getFixed(nums, reverse_edges)
            print(f"the following line was not safe {nums}, with {fixed}")
            res += getMiddle(fixed)

    print(res)