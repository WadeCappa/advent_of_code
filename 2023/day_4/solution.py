import sys
from functools import reduce

class Card:
    def __init__(self, number, yours, winning):
        self.number = number
        self.yours = yours 
        self.winning = winning

def arrayToNum(arr):
    return [int(x) for x in arr.split()]

def getCard(line):
    indexStr, numbersStr = line.split(":")
    return Card(int(indexStr.split()[-1]), arrayToNum(numbersStr.split("|")[0]), arrayToNum(numbersStr.split("|")[1]))

def getPoints(card):
    intersection = set(card.yours).intersection(card.winning)
    if len(intersection) == 0:
        return 0
    
    res = 1
    for _ in range(len(intersection) - 1):
        res *= 2
    return res

def getCopies(card):
    return len(set(card.yours).intersection(card.winning))

if __name__ == "__main__":
    input = sys.argv[1]
    cards = []
    with open(input) as f:
        for l in f:
            cards.append(getCard(l))
    
    copies = [1 for _ in cards]
    for i, c in enumerate(cards):
        copiesForCard = getCopies(c)
        for j in range(i + 1, min(i + copiesForCard + 1, len(copies))):
            copies[j] += copies[i]
    print(copies)
    print(reduce(lambda x, y: x + y, copies, 0))