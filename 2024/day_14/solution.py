import sys 

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

if __name__ == "__main__":
    file = sys.argv[1]
    wide = int(sys.argv[2])
    tall = int(sys.argv[3])
    its = int(sys.argv[4])
    content = ""
    with open(file) as f:
        content = f.read()
    robots = getRobots(content)
    print(robots)

    mid_x = wide // 2
    mid_y = tall // 2

    for i, _ in enumerate(robots):
        for _ in range(its):
            new_r = moveBot(robots[i], wide, tall)
            robots[i] = new_r
            print(new_r)

    res = 1
    q = 0
    for j in range(mid_y):
        for i in range(mid_x):
            for p, _ in robots:
                if (i, j) == p: 
                    print(p, mid_y, mid_x)
                    q += 1

    res *= q
    q = 0
    for j in range(mid_y + 1, tall):
        for i in range(mid_x):
            for p, _ in robots:
                if (i, j) == p: 
                    print(p, mid_y, mid_x)
                    q += 1

    res *= q
    q = 0
    for j in range(mid_y):
        for i in range(mid_x + 1, wide):
            for p, _ in robots:
                if (i, j) == p: 
                    print(p, mid_y, mid_x)
                    q += 1

    res *= q
    q = 0
    for j in range(mid_y + 1, tall):
        for i in range(mid_x + 1, wide):
            for p, _ in robots:
                if (i, j) == p: 
                    print(p, mid_y, mid_x)
                    q += 1

    res *= q
    q = 0
    print(res)