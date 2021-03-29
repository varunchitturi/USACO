x = int(input())
board = []
for i in range (x-1):
    toAppend = input().split()
    for j in range (len(toAppend)):
        toAppend[j] = int(toAppend[j])
    board.append(toAppend)
finals = []
for i in range (len(board)):
    finals.append(board[i][-1])
print (sum(finals)%2)
