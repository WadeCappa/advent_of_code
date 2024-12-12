from collections import defaultdict, deque
import sys

def getPerimeter(region):
    res = 0
    for y, x in region:
        for dy, dx in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            if (y + dy, x + dx) not in region:
                res += 1
    return res

def getPrice(region):
    c, region = region
    area = len(region)
    sides = 0

    seen = set()
    start = region[0]
    print(start)

    queue = deque([(start[0], start[1], {(1, 0): False, (0, 1): False, (-1, 0): False, (0, -1): False})])
    while len(queue) > 0:
        y, x, dirs = queue.popleft()
        if (y, x) in seen: 
            continue
        seen.add((y, x))
        if (y, x) not in region:
            continue
        for e in queue:
            if e[0] == y and e[1] == x:
                dirs = {d: dirs[d] or v for d, v in e[2].items()}
        print(y, x, sides, dirs)
        for d in dirs:
            dy, dx = d
            if (y + dy, x + dx) not in region:
                print(f"{y + dy}, {x + dx} not in region, with side {dirs[d]}")
                if not dirs[d]:
                    dirs[d] = True
                    sides += 1
            else:
                print(f"{y + dy}, {x + dx} in region, with side {dirs[d]}")
                dirs[d] = False
        for dy, dx in dirs:
            queue.append((y + dy, x + dx, dirs.copy()))

    print(c, sides, region)
    return sides * area

def getRegions(grid, max_y, max_x):
    res = []
    seen = set()

    def dfs(j, i, region, seen, c):
        if (j, i) in seen:
            return 
        if grid[(j, i)] != c:
            return
        seen.add((j, i))
        if grid[(j, i)] != c:
            return
        region.append((j, i))
        for dy, dx in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            dfs(j + dy, i + dx, region, seen, c)
        return

    for y in range(max_y):
        for x in range(max_x):
            if (y, x) in seen:
                continue
            region = []
            new_seen = set()
            c = grid[(y, x)]
            dfs(y, x, region, new_seen, c)
            seen = seen.union(new_seen)
            res.append((c, region))
    return res

if __name__ == "__main__":
    file = sys.argv[1]
    grid = defaultdict(lambda: '$')
    max_x = 0
    max_y = 0
    with open(file) as f:
        for j, l in enumerate(f):
            max_y = j
            for i, c in enumerate(l):
                grid[(j, i)] = c
                max_x = i
    max_x += 1
    max_y += 1
    
    regions = getRegions(grid, max_y, max_x)
    res = 0
    for r in regions:
        price = getPrice(r)
        res += price
    print(res)