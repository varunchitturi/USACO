def checkIfIn(list1,list2):
    for i in range (len(list1)):
        if list1[i] in list2:
            return False #if in return false
            break
    return True #if not in return True


def toColumn(l):
    columns = []

    for i in range (3):
        singleColumn = []
        for j in range (3):
            singleColumn.append(l[j][i])
        columns.append(singleColumn)
    return (columns)

def leftToRightDiagonal(l):
    diagonal=[]
    for i in range (3):
        diagonal.append(l[i][i])
    return diagonal

def rightToLeftDiagonal(l):
    diagonal = []
    diagonal.append(l[0][2])
    diagonal.append(l[1][1])
    diagonal.append(l[2][0])
    return diagonal


#initialize the game board
checkList1 = []
counterDoubleWin = 0
counterSingleWin = 0
board = []
for i in range(3):
    x,y,z = input()
    board.append([x,y,z])
#horizontal
for i in range (3):
    if len(set((board[i]))) == 1 and checkIfIn(checkList1,set(board[i])) == False:
        counterSingleWin += 1
        checkList1.append(set(board[i]))
        print(checkList1)
    elif len(set((board[i]))) == 2 and checkIfIn(checkList1,set(board[i]))==False:
        counterDoubleWin += 1
        checkList1.append(set(board[i]))
#verticals

verticalBoard = toColumn(board)

for i in range (3):
    if len(set(verticalBoard[i])) == 1 and checkIfIn(checkList1,set(verticalBoard[i])) == False:
        counterSingleWin += 1
        checkList1.append(set(verticalBoard[i]))
    elif len(set(verticalBoard[i])) == 2:
        counterDoubleWin += 1
        checkList1.append(set(verticalBoard[i]))
#diagonal forwards
diagonal1 = leftToRightDiagonal(board)
if len(set(diagonal1)) == 1 and checkIfIn(checkList1,set(diagonal1)) == False:
    counterSingleWin += 1
    checkList1.append(set(diagonal1))
elif len(set(diagonal1)) == 2 and checkIfIn(checkList1,set(diagonal1)):
    counterDoubleWin +=1
    checkList1.append(set(diagonal1))
#diagonal backwards
diagonal2 = rightToLeftDiagonal(board)
if len(set(diagonal2)) == 1 and checkIfIn(checkList1,set(diagonal2)) ==False:
    counterSingleWin+=1
    checkList1.append(set(diagonal2))
elif len(set(diagonal2)) == 2 and checkIfIn(checkList1,set(diagonal2)):
    counterDoubleWin +=1
    checkList1.append(set(diagonal2))
print (counterSingleWin)
print (counterDoubleWin)
