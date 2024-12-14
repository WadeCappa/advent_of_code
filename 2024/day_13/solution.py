import sys 

def solveWithMath(a, b, prize):
    x_1, x_2, x_r = a[0], b[0], prize[0]
    y_1, y_2, y_r = a[1], b[1], prize[1]

    xs = [x_1, x_2, x_r]
    ys = [y_1, y_2, y_r]
    print(xs, ys)

    for i, x in enumerate(xs):
        xs[i] = x * y_2
    for i, y in enumerate(ys):
        ys[i] = y * x_2
    
    print(xs, ys)

    a, res = xs[0] - ys[0], xs[2] - ys[2]
    a_mul = res // a
    print(a, res, a_mul)
    if res % a != 0:
        print(f"failed a mul! {a_mul / a}")
        return sys.maxsize

    b_mul = (y_r - (a_mul * y_1)) // y_2
    print(b_mul)
    if (y_r - (a_mul * y_1)) % y_2 != 0:
        print(f"failed b mul! {(y_r - (a_mul * y_1)) / y_2}")
        return sys.maxsize
    print(b_mul)

    print(a_mul * 3 + b_mul)
    return a_mul * 3 + b_mul

def getPrice(line):
    values = line.split(":")[-1]
    x, y = values.strip().split(",")
    return (int(x.strip().split("=")[-1]), int(y.strip().split("=")[-1]))

def getDeltas(line):
    values = line.split(":")[-1]
    x, y = values.strip().split(",")
    return (int(x.strip().split("+")[-1]), int(y.strip().split("+")[-1]))

def getGames(content):
    res = []
    for g in content.strip().split("\n\n"):
        a, b, prize = g.split("\n")
        a = getDeltas(a)
        b = getDeltas(b)
        prize = getPrice(prize)
        print(a, b, prize)
        res.append((a, b, prize))
    return res

def getOptimal(a, b, prize):
    memo = dict()

    def dfs(x, y, c):
        if (x, y, c) in memo: 
            return memo[(x, y, c)]
        if x == 0 and y == 0:
            return c
        if x < 0 or y < 0:
            return sys.maxsize
        best = sys.maxsize
        for button, cost in [(a, 3), (b, 1)]:
            dx, dy = button
            temp = dfs(x - dx, y - dy, c + cost)
            best = min(best, temp)
        memo[(x, y, c)] = best
        return best

    return dfs(prize[0], prize[1], 0)

if __name__ == "__main__":
    file = sys.argv[1]
    content = ""
    with open(file) as f:
        content = f.read()
    
    games = getGames(content)
    res = 0
    for a, b, prize in games:
        const = 10000000000000
        prize = (prize[0] + const, prize[1] + const)
        temp = solveWithMath(a, b, prize)
        print(temp)
        if temp == sys.maxsize:
            continue
        res += temp
    print(res)