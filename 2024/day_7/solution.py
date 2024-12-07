import sys 

def parse(l):
    ans, nums = l.split(":")
    return int(ans), [int(x) for x in nums.strip().split(" ")]

def isPossible(ans, nums):
    def add(i, t):
        return nums[i] + t

    def mul(i, t):
        return nums[i] * t

    def concat(i, t):
        return int(f"{t}{nums[i]}")

    def dfs(i, t):
        if i == len(nums) and t == ans:
            return True
        if i == len(nums):
            return False
        for op in [add, mul, concat]:
            if dfs(i + 1, op(i, t)):
                return True
        return False

    return dfs(1, nums[0])

if __name__ == "__main__":
    file = sys.argv[1]
    ops = []
    with open(file) as f:
        for l in f:
            ans, nums = parse(l)
            ops.append((ans, nums))

    res = 0
    for ans, nums in ops:
        if isPossible(ans, nums):
            res += ans
    print(res)