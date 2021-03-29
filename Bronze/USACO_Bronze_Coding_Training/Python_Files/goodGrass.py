import sys

#def squareSum(array,row,column):
#    for a in range
x,y = input().split()
rows = int(x)
columns = int(y)
field = []
for i in range (rows):
    x = input().split()
    field.append(x)
for i in range (len(field)):
    for j in range (len(field[0])):
        field[i][j] = int(field[i][j])
#print (field)
list = []
for i in range (rows-3):
    for j in range(columns-3):
        sum = 0
        sum += field[i][j]
        sum += field[i][j+1]
        sum += field[i][j+2]
        sum += field[i+1][j]
        sum += field[i+1][j+1]
        sum += field[i+1][j+2]
        sum += field[i+2][j]
        sum += field[i+2][j+1]
        sum += field[i+2][j+2]
        list.append([sum,[i+1,j+1]])
list.sort(reverse=True)
final = (list[0][0])
#print(list[0][1][0],end=" ")
#print(list[0][1][1],end=" ")
#print (field[2][1])
#print (list)
print (final)

for i in range (rows-3):
    for j in range(columns-3):
        sum = 0
        sum +=field[i][j]
        sum += field[i][j+1]
        sum += field[i][j+2]
        sum +=field[i+1][j]
        sum += field[i+1][j+1]
        sum += field[i+1][j+2]
        sum += field[i+2][j]
        sum += field[i+2][j+1]
        sum += field[i+2][j+2]
        if sum == final:

            print (i+1,end=" ")
            print (j+1)
            sys.exit()
