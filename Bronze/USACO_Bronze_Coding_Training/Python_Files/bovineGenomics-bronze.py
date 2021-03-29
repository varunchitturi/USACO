def toColumn(list):
    columns = []

    for i in range (len(list[0])):
        singleColumn = []
        for j in range (len(list)):
            singleColumn.append(list[j][i])
        columns.append(singleColumn)
    return (columns)
x,y = input().split()
numSpottyGenes = int(x)
numPlainGenes = int(x)
numGenes = int(y)
spottyGenes = []
plainGenes = []
check = "true"
counter = 0
for i in range (numSpottyGenes):
    x = list(input())
    spottyGenes.append(x)
for i in range (numPlainGenes):
    x = list(input())
    plainGenes.append(x)



#print (spottyGenes)
#print (plainGenes)
#print (numPlainGenes)
#print(numGenes)
hi = toColumn(plainGenes)
for i in range(numGenes):
    check = "true"
    for j in range (numPlainGenes):
        if spottyGenes[j][i] in hi[i]:
            check = "false"
            break
    if check == "true":
        counter += 1
        #print (i)
print (counter)
