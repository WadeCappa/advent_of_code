import sys

class Springs:
    def __init__(self, row, groups, co):
        self.row = row
        self.groups = groups
        self.co = co
    
    def __repr__(self):
        return f"{self.row}, {','.join([str(x) for x in self.groups])}"

    def __isValid(self, r):
        newGroups = []
        last = 0
        curr = '.'
        for loop in range(self.co):
            for i, c in enumerate(r):
                if c != curr and curr == '#':
                    newGroups.append(i - last)
                if c == '.':
                    curr = '.'
                    last = i
                if c != curr and curr == '.':
                    last = i
                    curr = '#'
            if curr == '#':
                newGroups.append(len(r) - last)

        return newGroups == self.groups

    def getValidCombos(self):
        allRows = []
        def dfs(i, p):
            if i == len(self.row):
                allRows.append(p)
                return
            if self.row[i] == '?':
                dfs(i + 1, p + ['#'])
                dfs(i + 1, p + ['.'])
            else:
                dfs(i + 1, p + [self.row[i]])
        dfs(0, [])
        return len([x for x in allRows if self.__isValid(x)])

def loadInput(file, co):
    res = []
    with open(file) as f:
        for l in f:
            row, code = l.split()
            res.append(Springs(row, [int(x) for x in code.split(",")], co))
    return res

if __name__ == "__main__":
    file = sys.argv[1]
    co = int(sys.argv[2])
    springs = loadInput(file, co)
    res = 0
    for s in springs:
        total = s.getValidCombos()
        print(f"{total} for {s}")
        res += total
    print(res)