from collections import defaultdict
import sys

# p2 (10, 11)
# p1 (12, 9)
# d  (-2, 2)

def inBounds(grid, y, x):
    return grid[(y, x)] != "&"

def getDistance(p2, p1):
    y1, x1 = p1
    y2, x2 = p2
    return ((y2 - y1), (x2 - x1))

def findPairs(locations, grid):
    pairs = set()
    for y1, x1 in locations:
        for y2, x2 in locations:
            if (y1, x1) == (y2, x2):
                continue
            dy, dx = getDistance((y2, x2), (y1, x1))
            temp_y, temp_x = y2, x2
            while inBounds(grid, temp_y + dy, temp_x + dx):
                pairs.add((temp_y + dy, temp_x + dx))
                temp_y, temp_x = temp_y + dy, temp_x + dx
            temp_y, temp_x = y1, x1
            while inBounds(grid, temp_y - dy, temp_x - dx):
                pairs.add((y1 - dy, x1 - dx))
                temp_y, temp_x = temp_y - dy, temp_x - dx

    return pairs

if __name__ == "__main__":
    file = sys.argv[1]
    grid = defaultdict(lambda: "&")
    freqLocations = defaultdict(list)

    freqs = set()

    with open(file) as f:
        for j, l in enumerate(f):
            for i, c in enumerate(l.strip()):
                grid[(j, i)] = c
                if c != ".":
                    freqs.add(c)
                    freqLocations[c].append((j, i))
    
    pairs = set()
    for f in freqs:
        pairs = pairs.union(findPairs(freqLocations[f], grid))
        pairs = pairs.union(set(freqLocations[f]))
    print(len(pairs))