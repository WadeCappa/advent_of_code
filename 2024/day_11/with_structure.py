import sys 

def blink(stone, its, memo):
    if its == 0:
        return 1
    if (stone, its) in memo:
        return memo[(stone, its)]

    res = 0
    s = str(stone)

    if stone == 0:
        res += blink(1, its - 1, memo)
    elif (len(s) % 2) == 0:
        right = s[len(s) // 2:]
        left = s[:len(s) // 2]
        res += blink(int(left), its - 1, memo)
        res += blink(int(right), its - 1, memo)
    else:
        res += blink(int(s) * 2024, its - 1, memo)
    memo[(stone, its)] = res
    return res

if __name__ == "__main__":
    file, its = sys.argv[1], int(sys.argv[2]) 

    stones = ""
    with open(file) as f:
        stones = [int(x) for x in f.read().strip().split()]
    print(stones)
    res = 0
    memo = {}
    for s in stones:
        res += blink(s, its, memo)
    print(res)