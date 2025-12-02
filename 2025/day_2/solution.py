from functools import reduce
import sys

def isValidBruteForce(num):
    input = str(num)
    for i in range(1, len(input)):
        word = input[0:i]
        res = input.split(word)
        if len(res) > 0 and reduce(lambda x, y: y == '' and x, res, True):
            return False
    return True

if __name__ == "__main__":
    file = sys.argv[1]
    ranges = []
    with open(file) as f:
        ranges = [[int(y) for y in x.split('-')] for x in f.read().split(",")]
    
    total = 0
    for r in ranges:
        start = r[0]
        end = r[1]
        while start <= end:
            if not isValidBruteForce(start):
                total += start
            start += 1
    print(total)
