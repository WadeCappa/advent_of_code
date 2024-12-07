import sys
from collections import deque

down = (1, 0)
up = (-1, 0)
left = (0, -1)
right = (0, 1)

pipe_parts = {
    '|': [up, down],
    '-': [right, left],
    'L': [up, right],
    'J': [up, left],
    '7': [down, left],
    'F': [down, right]
}

def applyMove(pos, move):
    return (pos[0] + move[0], pos[1] + move[1])

def extrapolatePipe(pipes, p):
    j, i = p
    inverse_moves = []
    print(p)
    print(pipes)
    if j > 0 and pipes[j-1][i] in pipe_parts and down in pipe_parts[pipes[j-1][i]]:
        inverse_moves.append(up)
    if i < len(pipes[j]) - 1 and pipes[j][i+1] in pipe_parts and left in pipe_parts[pipes[j][i+1]]:
        inverse_moves.append(right)
    if j < len(pipes) - 1 and pipes[j+1][i] in pipe_parts and up in pipe_parts[pipes[j+1][i]]:
        inverse_moves.append(down)
    if i > 0 and pipes[j][i-1] in pipe_parts and right in pipe_parts[pipes[j][i-1]]:
        inverse_moves.append(left)

    for k, v in pipe_parts.items():
        if sorted(v) == sorted(inverse_moves):
            print(f"starting with pipe {k} with moves of {inverse_moves}")
            return k
    print(f"could not find pipe part with {inverse_moves}")

def getPipeBounds(pipes, start):
    seen = set()
    bounds = []
    for _ in pipes:
        bounds.append([])
    positions = deque([(start[0], start[1])])
    while positions:
        j, i = positions.pop()
        if (j, i) in seen:
            continue
        seen.add((j, i))
        bounds[j].append(i)
        for move in pipe_parts[pipes[j][i]]:
            nj, ni = applyMove((j, i), move)
            positions.appendleft((nj, ni))
    
    for i, _ in enumerate(bounds):
        bounds[i] = sorted(bounds[i])
    return seen 

def findFarthestPart(pipes, start):
    seen = set()
    positions = deque([(start[0], start[1], 0)])
    max_distance = 0
    while positions:
        j, i, distance = positions.pop()
        if (j, i) in seen:
            continue
        max_distance = max(max_distance, distance)
        seen.add((j, i))
        for move in pipe_parts[pipes[j][i]]:
            nj, ni = applyMove((j, i), move)
            positions.appendleft((nj, ni, distance + 1))
    
    return max_distance 

def isEnclosed(pipes, bounds, point):
    if point in bounds:
        return False
    y, x = point
    xfront, xback = 0, 0
    yfront, yback = 0, 0
    for i in range(len(pipes[y])):
        if (y, i) in bounds and pipes[y][i] != '-':
            if i < x:
                xfront += 1
            else:
                xback += 1
    for j in range(len(pipes)):
        if (j, x) in bounds and pipes[j][x] != '|':
            if j < y:
                yfront += 1
            else:
                yback += 1
    print(f"looking at point {point} -> xfront: {xfront}, xback: {xback}, yfront: {yfront}, yback: {yback}")
    if 0 in [yfront, yback, xfront, xback]:
        return False
    return xfront % 2 != 0 or yfront % 2 != 0 or xback % 2 != 0 or yback % 2 != 0


def getEnclosed(pipes, bounds):
    enclosed = set()
    for y in range(len(pipes)):
        for x in range(len(pipes[y])):
            if isEnclosed(pipes, bounds, (y, x)):
                enclosed.add((y, x))

    return enclosed

if __name__ == "__main__":
    input = sys.argv[1]
    pipes = []
    start = None
    with open(input) as f:
        j = 0
        for l in f:
            if 'S' in l:
                start = (j, l.find('S'))
            pipes.append([x for x in l.replace('\n', '')])
            print(pipes[-1])
            j += 1

    starting_pipe = extrapolatePipe(pipes, start)
    print(f"starting at {starting_pipe}")
    pipes[start[0]][start[1]] = starting_pipe
    bounds = getPipeBounds(pipes, start)
    print(bounds)
    enclosed = getEnclosed(pipes, bounds)
    print(enclosed)
    print(len(enclosed))