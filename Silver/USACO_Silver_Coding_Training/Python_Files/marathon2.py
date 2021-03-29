numCheckpoints = int(input())
checkPoints = []
for i in range(numCheckpoints):
    x,y = input().split()
    checkPoints.append([int(x),int(y)])
minimumDistance = 999999999999999999999999999
distance = 0
for i in range(len(checkPoints)-1):
    distance += abs(checkPoints[i][0] - checkPoints[i+1][0]) + abs(checkPoints[i][1] - checkPoints[i+1][1])
for i in range(len(checkPoints)-2):
    checkDist = distance - abs(checkPoints[i][0] - checkPoints[i+1][0]) - abs(checkPoints[i][1] - checkPoints[i+1][1]) - abs(checkPoints[i+1][0] - checkPoints[i+2][0]) - abs(checkPoints[i+1][1] - checkPoints[i+2][1]) + abs(checkPoints[i][0] - checkPoints[i+2][0]) + abs(checkPoints[i][1] - checkPoints[i+2][1])
    if checkDist < minimumDistance:
        minimumDistance = checkDist
print(minimumDistance)


