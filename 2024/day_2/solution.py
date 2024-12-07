import sys

def isLevelValid(l):
    def dfs(i, last, increasing, hasSkip):
        if i >= len(l):
            return True 
        print(i, last, increasing, hasSkip)
        change = l[i] - l[last] if increasing else l[last] - l[i]
        if change > 3 or change < 1:
            if hasSkip:
                return dfs(i + 1, last, increasing, False)
            return False
        return dfs(i + 1, i, increasing, hasSkip)

    for inc in [True, False]:
        print(f"{inc} for {l}")
        if dfs(1, 0, inc, True) or dfs(2, 1, inc, False):
            print(f"{l} is safe")
            return True
    return False

if __name__ == "__main__":
    file = sys.argv[1]
    levels = []
    with open(file) as f:
        for l in f:
            levels.append([int(x) for x in l.split()])
    print(levels)
    res = 0
    for l in levels:
        isValid = isLevelValid(l)
        print(l, isValid)
        res += isValid
    print(res)