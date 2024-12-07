import sys
from functools import reduce

class Game:
    def __init__(self, number, reveals):
        self.number = number 
        self.reveals = reveals

def getTotalCubes():
    return {
        "red": 12,
        "green": 13,
        "blue": 14
    }

def revealAsDict(line):
    tokens = line.split(",")
    res = dict()
    for token in tokens:
        quantity, color = token.split()
        res[color] = int(quantity)
    return res

def parseLine(line):
    game, reveals = line.split(":")
    return Game(int(game.split()[1]), [revealAsDict(x) for x in reveals.split(";")])

def isGamePossible(game, totalCubes):
    for reveal in game.reveals:
        for color in reveal.keys():
            if color not in totalCubes or totalCubes[color] < reveal[color]:
                return False
    return True

def getMinimumSetToMakeGamePossible(game):
    minimalSet = {"green":0, "blue":0, "red":0}
    for reveal in game.reveals:
        for color in reveal.keys():
            if color not in minimalSet:
                print("error, expected color to be in minimal set")
            minimalSet[color] = max(minimalSet[color], reveal[color])
    return reduce(lambda x, y: x * y, minimalSet.values(), 1)

if __name__ == "__main__":
    input = sys.argv[1]
    sum = 0
    totalCubes = getTotalCubes()
    with open(input) as f:
        for l in f:
            g = parseLine(l)
            sum += getMinimumSetToMakeGamePossible(g)

    print(sum)