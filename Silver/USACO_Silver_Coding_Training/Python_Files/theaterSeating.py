x,y = input().split()
width = int(x)
numRows = int(y)
bestPositions = (width-1)//2

finalPriority = []
seats = []
for i in range(numRows):
    new = []
    for j in range(width):
        seats.append([abs(i-0)**2+abs(j-bestPositions)**2,i,j])
        new.append(0)
    finalPriority.append(new)

seats.sort()
#print(new)
#print(len(finalPriority))
for i in range(len(seats)):
    finalPriority[seats[i][1]][seats[i][2]] = i + 1

finalPriority.reverse()

for i in range(len(finalPriority)):
    for j in range(width):
        print(finalPriority[i][j], end=" ")
    print()



