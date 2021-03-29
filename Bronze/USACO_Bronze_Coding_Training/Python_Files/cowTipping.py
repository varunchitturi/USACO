def flip(array,i,j):
    for a in range (i+1):
        for b in range (j + 1):
            if array[a][b] == 1:
                array[a][b] = 0
            else:
                array[a][b] = 1
    return field
size = int(input())
field = []
for i in range (size):
    field.append(list(input()))
for i in range (size):
    for j in range (size):
        field[i][j] = int(field[i][j])


flipCounter = 0







for i in range (size-1,-1,-1):
    for j in range(size-1,-1,-1):
        if field[i][j] == 1:
            field = flip(field,i,j)
            flipCounter += 1
#print (field)
print (flipCounter)
