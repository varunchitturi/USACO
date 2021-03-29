import copy
import sys


def toColumn(list):
    columns = []

    for i in range(len(list[0])):
        singleColumn = []
        for j in range(len(list)):
            singleColumn.append(list[j][i])
        columns.append(singleColumn)
    return (columns)


x, y = input().split()
numPieces = int(y)
gridLength = int(x)
pieces = []
original = []
for i in range(gridLength):
    original.append(list(input()))
for i in range(numPieces):
    grid = []
    for j in range(gridLength):
        grid.append(list(input()))
    pieces.append(grid)
# print (original)
# print (pieces)


def getStartPos(grid1):
    columnGrid = toColumn(grid1)
    for i in range(gridLength):
        if "#" in grid1[i]:
            topBorder = i
            break
    for i in range(gridLength):
        if "#" in columnGrid[i]:
            leftBorder = i
            break
    # shift up
    for i in range(0, topBorder):
        grid1.append(grid1[0])
        del grid1[0]
    # shift left
    for i in range(0, leftBorder):
        for j in range(gridLength):
            grid1[j].append(grid1[j][0])
            del grid1[j][0]
    return (grid1)


# set all pieces to start position
for i in range(len(pieces)):
    pieces[i] = getStartPos(pieces[i])


allGrids = []
for i in range(len(pieces)):
    toAppend = []
    grid = copy.deepcopy(pieces[i])
    columnGrid = toColumn(grid)
    # get left border
    for j in range(len(columnGrid)-1, -1, -1):
        if '#' in columnGrid[j]:
            rightBorder = j
            break
    # get bottom border
    for j in range(gridLength-1, -1, -1):
        if "#" in grid[j]:
            bottomBorder = j
            break
    gridReset = copy.deepcopy(grid)
    for j in range(gridLength-bottomBorder):
        if j != 0:
            grid = copy.deepcopy(gridReset)
            grid.insert(0, grid[-1])
            del grid[-1]
            gridReset = copy.deepcopy(grid)
        for k in range(gridLength-rightBorder):
            if k != 0:
                for a in range(gridLength):
                    grid[a].insert(0, grid[a][-1])
                    del grid[a][-1]

            toAppend.append(copy.deepcopy(grid))
    allGrids.append(toAppend)


# print (pieces)
# print (allGrids)


def combinePieces(grid1, grid2):
    newGrid = []
    for i in range(gridLength):
        appendTo = []
        for j in range(gridLength):
            appendTo.append('.')
        newGrid.append(appendTo)
    for i in range(gridLength):
        for j in range(gridLength):
            if (grid1[i][j] == '#') or (grid2[i][j] == '#'):
                newGrid[i][j] = '#'
    return newGrid


for i in range(len(allGrids)):
    for j in range(i+1, len(allGrids)):
        piece1 = allGrids[i]
        piece2 = allGrids[j]
        for a in range(len(piece1)):
            for b in range(len(piece2)):
                if combinePieces(piece1[a], piece2[b]) == original:
                    final = [i+1, j+1]
                    print (min(final), end=" ")
                    print (max(final))
                    sys.exit()
