import copy


def toColumn(list):
    columns = []

    for i in range(len(list[0])):
        singleColumn = []
        for j in range(len(list)):
            singleColumn.append(list[j][i])
        columns.append(singleColumn)
    return (columns)


# inputs
sideLength = int(input())
canvasr = []
for i in range(sideLength):
    x = input()

    canvasr.append(x)
canvas = []
for i in range(len(canvasr)):
    toAppend = []
    for j in range(len(canvasr[i])):
        toAppend.append(canvasr[i][j])
    canvas.append(toAppend)
colors = []
for i in range(sideLength):
    for j in range(sideLength):
        colors.append(canvas[i][j])
colors = list(set(colors))
if '0' in colors:
    colors.remove('0')

possibles = []
for i in range(len(colors)):
    possibles.append(colors[i])
# dimensions constructer


def createDimensions(board, colorsr):
    dimensions = []
    for i in range(len(colorsr)):
        toAppend = [0, 0, 0, 0, 0, 0]
        toAppend[0] = colorsr[i]
        # define the width
        for j in range(sideLength):
            if colorsr[i] in (toColumn(board))[j]:
                start = j
                break
        for j in range(sideLength-1, -1, -1):
            if colorsr[i] in (toColumn(board))[j]:
                end = j
                break

        width = end - start + 1
        # define the length
        for j in range(sideLength):
            if colorsr[i] in board[j]:
                start = j
                break
        for j in range(sideLength-1, -1, -1):
            if colorsr[i] in board[j]:
                end = j
                break
        length = end - start + 1
        # get start index
        check = False
        for j in range(sideLength):
            if colorsr[i] in board[j]:
                startRow = j
                break
        for j in range(sideLength):
            if colorsr[i] in (toColumn(board))[j]:
                startColumn = j
                break
        # check if it is a complete rectangle
        elements = []
        for j in range(startRow, startRow + length):
            for k in range(startColumn, startColumn + width):
                elements.append(board[j][k])
        if len(list(set(elements))) == 1:
            isRectangle = True
        else:
            isRectangle = False

        # initialize a single colors dimension
        toAppend[1] = width
        toAppend[2] = length
        toAppend[3] = startRow
        toAppend[4] = startColumn
        toAppend[5] = isRectangle
        dimensions.append(toAppend)
    return (dimensions)
def check(color1, color2):
    dimensions = createDimensions(canvas, colors)
    for i in range(len(dimensions)):
        if dimensions[i][0] == color2:
            check = i
            break
        else:
            check = -1
    if check != -1:
        for i in range(dimensions[check][3], dimensions[check][3] + dimensions[check][2]):
            for j in range(dimensions[check][4], dimensions[check][4] + dimensions[check][1]):
                if canvas[i][j] == color1:
                    return True
        return False


for i in range(len(colors)):
    for j in range(len(colors)):
        if i!= j and check(colors[i], colors[j]) is True:
            if colors[i] in possibles:
                possibles.remove(colors[i])

print (len(possibles))
