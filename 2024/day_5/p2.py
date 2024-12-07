import sys

def sortBad(line, edges):
    nums = [int(x) for x in line.split(",")]
    reversed_nums = nums[::-1]
    placements = {l: i for i, l in enumerate(nums)}
    res = []
    for n, i in placements.items():  
        print(n, edges)
        if n not in edges:
            res.append(n)
            continue
        for e in edges[n]:
            if e in placements and placements[e] < placements[n]:
                res.append(e)
    return res

def isSafe(line, edges):
    placements = {l: i for i, l in enumerate([int(x) for x in line.split(",")])}
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

def getMiddle(line):
    nums = [int(x) for x in line.split(",")]
    return nums[len(nums) // 2]

if __name__ == "__main__":
    file = sys.argv[1]
    data = ""
    with open(file) as f:
        data =f.read()
    paths, lines = data.split("\n\n")
    d = {}
    print(paths)
    for p in paths.split("\n"):
        print(p)
        l, r = p.split("|")
        l, r = int(l), int(r)
        if l not in d:
            d[l] = []
        d[l].append(r)
    print(d)

    res = 0
    original_res = 0
    for l in lines.split("\n"):
        print(l)
        if not isSafe(l, d):
            new_l = sortBad(l, d)
            print(f"the following is not safe: {l}, better as got {new_l}")
            res += getMiddle(','.join(str(x) for x in new_l))
        else:
            original_res += getMiddle(l)

    print(res)
    print(original_res)