
numCows = int(input())

allCoordinates = []

XVals = []
YVals = []
for i in range(numCows):
    coordinates = input().split()
    for j in range(2):
        coordinates[j] = int(coordinates[j])
    allCoordinates.append(coordinates)
    XVals.append(coordinates[0])
    YVals.append(coordinates[1])
xmin = XVals[0]
ymin = YVals[0]
xmax = XVals[-1]
ymax = YVals[-1]
area = 999999999999

XVals.sort()
YVals.sort()

for i in range(numCows):
    xmin = XVals[0]
    xmax = XVals[-1]
    ymin = YVals[0]
    ymax = YVals[-1]
    if allCoordinates[i][0] == XVals[0]:
        xmin = XVals[1]

    if allCoordinates[i][0] == XVals[-1]:
        xmax = XVals[-2]

    if allCoordinates[i][1] == YVals[0]:
        ymin = YVals[1]

    if allCoordinates[i][1] == YVals[-1]:
        ymax = YVals[-2]

    if area > (xmax-xmin)*(ymax-ymin):
        area = (xmax-xmin)*(ymax-ymin)
print(area)
