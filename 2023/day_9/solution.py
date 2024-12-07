from functools import reduce
import sys

def getRateOfChange(sequence):
    rateOfChange = []
    for i in range(1, len(sequence)):
        rateOfChange.append(sequence[i] - sequence[i - 1])

    if reduce(lambda a, b: a + b, rateOfChange, 0) != 0:
        deeperRateOfChange = getRateOfChange(rateOfChange)
        rateOfChange.append(rateOfChange[-1] + deeperRateOfChange[-1])
    
    return rateOfChange

def getNextElement(sequence):
    roc = getRateOfChange(sequence)
    return sequence[-1] + roc[-1]

if __name__ == "__main__":
    input = sys.argv[1]
    sequences = []
    with open(input) as f:
        sequences = [[int(x) for x in l.split()] for l in f]
    res = 0
    for s in sequences:
        nextElem = getNextElement(s[::-1])
        res += nextElem
        print(f"{s}, next element of {nextElem}")
    print(res)
