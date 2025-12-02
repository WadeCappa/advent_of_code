
import sys
from collections import deque

def loadMaze(file):
    with open(file, "r") as f:
        return [list(l) for l in f]

def findStart(maze):
    for y, line in enumerate(maze):
        for x, p in enumerate(line):
            if p == "S":
                return (y, x)

def getNextDirections(direction):
    if direction == '>' or direction == '<':
        return ('^', 'v')
    elif direction == '^' or direction == 'v':
        return ('<', '>')

def getDyDx(direction):
    if direction == '>':
        return (0, 1)
    if direction == '^':
        return (-1, 0)
    if direction == '<':
        return (0, -1)
    if direction == 'v':
        return (1, 0)

def dfs(maze, start):
    seen = set()
    y, x = start
    q = deque((x, y, '>', 0))
    while len(q) > 0:
        y, x, direction, score = q.pop()
        nextDirections = getNextDirections(direction)

if __name__ == "__main__":
    file = sys.argv[1]
    maze = loadMaze(file)
    start = findStart(maze)
    print(start)
