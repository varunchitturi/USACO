def checkLessGreat(coordiates,xVal):
    leftRight = [0,0]
    for i in range (len(coordiates)):
        if coordiates[i] > xVal:
            leftRight[1] += 1
        else:
            leftRight[0] += 1
        leftRight[0] += 1
        leftRight[1] += 1
    return leftRight
import math
import statistics
x,y = input().split()
numCoordintates = int(x)
greatestCoordinate = int(y)
xCoord = []
yCoord = []
upperLeft = 0
upperRight = 0
lowerLeft = 0
lowerRight = 0
for i in range (numCoordintates):
    x,y = input().split()
    xCoord.append(int(x))
    yCoord.append(int(y))


xVal = 0
yVal = 0
maximum = 9999999999999

for a in range (len(xCoord)):
    xVal = xCoord[a] +1
    for j in range (len(yCoord)):
        yVal = yCoord[j] +1
        upperRight = 0
        upperLeft = 0
        lowerLeft = 0
        lowerRight = 0
        for i in range (numCoordintates):
            #upperLeft
            if xCoord[i] < xVal and yCoord[i] > yVal:
                upperLeft += 1
            #upperRight
            if xCoord[i] > xVal and yCoord[i] > yVal:
                upperRight += 1
            #lowerLeft
            if xCoord[i] < xVal and yCoord[i] < yVal:
                lowerLeft += 1
            #lowerRight
            if xCoord[i] > xVal and yCoord[i] < yVal:
                lowerRight += 1


        totals = [upperRight,upperLeft,lowerRight,lowerLeft]
        if maximum > max(totals):
            maximum = max(totals)
print (maximum)
