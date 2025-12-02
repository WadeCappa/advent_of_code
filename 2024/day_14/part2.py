import time
import sys 

def printGrid(robots, wide, tall):
    for i in range(wide):
        row = []
        for j in range(tall):
            count = 0
            for p, _ in robots:
                if p == (i, j):
                    count += 1
            row.append(count if count != 0 else ".")
        print(''.join([str(x) for x in row]))

def moveBot(robot, wide, tall):
    p, v = robot
    x, y = p
    dx, dy = v
    new_x = (x + dx) % wide
    new_y = (y + dy) % tall
    return ((new_x, new_y), v)

def getCoords(line):
    x, y = line.split(",")
    return (int(x.split("=")[-1]), int(y))

def getRobots(content):
    res = []
    content.strip()
    for r in content.split("\n"):
        p, v = r.split(" ")
        res.append((getCoords(p), getCoords(v)))
    return res

def getQuad(robots, mid_y, mid_x):
    res = []
    q = 0
    for j in range(mid_y):
        for i in range(mid_x):
            for p, _ in robots:
                if (i, j) == p: 
                    q += 1

    res.append(q)
    q = 0
    for j in range(mid_y + 1, tall):
        for i in range(mid_x):
            for p, _ in robots:
                if (i, j) == p: 
                    q += 1

    res.append(q)
    q = 0
    for j in range(mid_y):
        for i in range(mid_x + 1, wide):
            for p, _ in robots:
                if (i, j) == p: 
                    q += 1

    res.append(q)
    q = 0
    for j in range(mid_y + 1, tall):
        for i in range(mid_x + 1, wide):
            for p, _ in robots:
                if (i, j) == p: 
                    q += 1
    res.append(q)
    return res

def thresh(qs):
    diff = 0
    for v in qs:
        diff = abs(diff - v)
    print(diff)
    return diff > 200

if __name__ == "__main__":
    file = sys.argv[1]
    wide = int(sys.argv[2])
    tall = int(sys.argv[3])
    start = int(sys.argv[4])
    content = ""
    with open(file) as f:
        content = f.read()
    robots = getRobots(content)
    print(robots)

    mid_x = wide // 2
    mid_y = tall // 2

    it = 0
    while True:
        print(it)
        for i, _ in enumerate(robots):
            new_r = moveBot(robots[i], wide, tall)
            robots[i] = new_r
        if it > start:
            qs = getQuad(robots, mid_y, mid_x)
            if thresh(qs):
                print(it, qs)
                printGrid(robots, wide, tall)
        it += 1
