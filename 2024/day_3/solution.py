from functools import reduce
from collections import deque
import sys 

mul_op = "mul(X,Y)"
enable_op = "do()"
disable_op = "don't()"

def isValidNum(n):
    return n.isnumeric() and len(n) >= 1 and len(n) <= 3

def findNextMul(line, i):
    tokens = line[i:].split("mul(")[1:]
    print(f"looking at {line[i:]}")
    for t in tokens:
        muls = t.split(")")
        if len(muls) == 0:
            continue
        nums = muls[0].split(",")
        if len(nums) != 2:
            continue
        x, y = nums
        if isValidNum(x) and isValidNum(y):
            next = line[i:].find(f"mul({x},{y})") + i
            print(f"found mul at {next} with {x} and {y}: {line[next:next+15]}")
            return (next, int(x) * int(y), line[next:next+15])
    return (-1, 0, "")

def findAllMuls(line):
    res = []
    p = 0
    while p < len(line):
        next, v, s = findNextMul(line, p)
        if next == -1:
            break
        res.append((next, v, s))
        p = next + 5
    return res

def getMul(line):
    res = 0
    p = 0
    line = "do()" + line
    while p < len(line):
        start = line[p:].find(enable_op)
        if start == -1:
            break
        start += p
        stop = line[start:].find(disable_op) 
        if stop == -1:
            stop = len(line) - 1
        else:
            stop += start
        print(f"range of {(start, stop)}")
        vals = findAllMuls(line[start:stop + 1])
        total = reduce(lambda t, x: t + x[1], vals, 0)
        print(f"vals of {vals} of total {total}")
        res += total
        p = stop + 1
    return res

if __name__ == "__main__":
    file = sys.argv[1]
    res = 0
    with open(file) as f:
        content = ''.join([l.strip() for l in f])
        print(content)
        res += getMul(content)
    print(res)