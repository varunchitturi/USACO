x,y,z = input().split()
columns = int(x)
rows = int(y)
plows = int(z)
array = []
firstXY = []
secondXY = []
for i in range (rows):
    toAppend = []
    for j in range (columns):
        toAppend.append(0)
    array.append(toAppend)
for i in range (plows):
    a,b,c,d = input().split()
    firstXY.append([int(a)-1,int(b)-1])
    secondXY.append([int(c)-1,int(d)-1])
for i in range (plows):
    startX = firstXY[i][0]
    startY = firstXY[i][1]
    stopX = secondXY[i][0]
    stopY = secondXY[i][1]
    for j in range (startY,stopY+1):
        for k in range (startX,stopX+1):
            array[j][k] = 1
totals = 0
for i in range (len(array)):
    totals += sum(array[i])
print (totals)
