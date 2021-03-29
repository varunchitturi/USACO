
x, y = input().split()
bullArray = []
cowArray = []
numBulls = int(x)
numCows = int(y)
allArray = []
for i in range(numBulls):
    a = input()
    bullArray.append(a)
    allArray.append(a)
for i in range(numCows):
    a = input()
    cowArray.append(a)
    allArray.append(a)
printMatrix = []
for i in range(numBulls):
    appendTo = []
    for j in range(numCows):
        appendTo.append(0)
    printMatrix.append(appendTo)
# print (printMatrix)
for i in range(numBulls):
    for j in range(numCows):
        mother = cowArray[j]
        father = bullArray[i]
        for k in range(len(allArray)):
            check = True
            if k-numBulls != j and k != i:
                for l in range(25):
                    # print (allArray[k][l])
                    # print ([i,j,k,l])
                    if allArray[k][l] != mother[l] and allArray[k][l] != father[l]:
                        check = False
                        break
                if check is True:
                    printMatrix[i][j] += 1

for i in range(len(printMatrix)):
    for j in range(len(printMatrix[i])):
        if j != len(printMatrix[i]) - 1:
            print(printMatrix[i][j], end=" ")
        else:
            print(printMatrix[i][j])
