
import sys
import math

def handle_instructions(instructions, start):
    r = 0
    c = start
    for i in instructions.split():
        d = i[0]
        total = int(i[1:])
        if d == 'L':
            total = 0 - total
        if (c + total) % 100 == 0:
            a = total
            if a < 0:
                a = 0 - a
            if a >= 100:
                r += a // 100
            else:
                r += 1
        elif c + total >= 100:
            r += math.ceil(total / 100)
        elif c + total <= 0:
            if c == 0 and total < 100:
                pass
            else:
                r += math.ceil((0 - total) / 100)
                if c == 0:
                    r -= 1
        c = (c + total) % 100
        print(c, total, i, r)
    return r

if __name__ == "__main__":
    file = sys.argv[1]
    content =""
    with open(file) as f:
         content = f.read()
    start = 50

    print(handle_instructions(content, start))
