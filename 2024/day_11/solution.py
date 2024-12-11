import sys 

def blink(stones):
    res = []
    for s in stones:
        if s == 0:
            res.append(1)
        elif (len(str(s)) % 2) == 0:
            string = str(s)
            right = string[len(string) // 2:]
            left = string[:len(string) // 2]
            res.append(int(left))
            res.append(int(right))
        else:
            res.append(s * 2024)
    return res

if __name__ == "__main__":
    file = sys.argv[1]
    stones = ""
    with open(file) as f:
        stones = [int(x) for x in f.read().strip().split()]
    print(stones)
    for i in range(75):
        stones = blink(stones)
        print(i, len(stones))
    print(len(stones))