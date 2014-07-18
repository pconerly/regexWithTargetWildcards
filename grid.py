import math


class HexGrid:
    def __init__(self, start):
        self.grid = {}
        self.limit = self.posAbs(start) + 1
        self.dirFuncs = [self.moveEast, self.moveSouthEast, self.moveSouthWest]

    def moveEast(self, coords):
        coords = list(coords)
        coords[0] += 1
        coords[1] -= 1
        return tuple(coords)

    def moveSouthEast(self, coords):
        coords = list(coords)
        coords[1] -= 1
        coords[2] += 1
        return tuple(coords)

    def moveSouthWest(self, coords):
        coords = list(coords)
        coords[0] -= 1
        coords[2] += 1
        return tuple(coords)

    def posAbs(self, coords):
        return int(sum([math.fabs(i) for i in coords]))

    def explore(self, pos):
        self.grid[pos] = True
        for dirFunc in self.dirFuncs:
            newPos = dirFunc(pos)
            newAbs = self.posAbs(newPos)
            if newAbs <= self.limit and not self.grid.has_key(newPos):
                self.explore(newPos)

        return self.grid

    def spacesInAHex(self, leg):
        spaces = 0
        diameter = 2*leg - 1
        for i in range(leg, diameter):
            spaces += 2*i
        spaces += diameter
        return spaces

if __name__ == "__main__":
    start = (0, 6, -6)
    hg = HexGrid(start)
    grid = hg.explore(start)
    for key in grid.keys():
        print key
    print "----"
    print "%s keys" % len(grid)
    total = hg.spacesInAHex(7)
    print total
    print total - len(grid)




