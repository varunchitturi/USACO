import copy
numDirections = int(input())
directions = []
for i in range(numDirections):
    x, y = input().split()
    directions.append([x, int(y)])
currentPosition = [0, 0]
time = 0
positionAndTime = []
for i in range(len(directions)):
    for j in range(directions[i][1]):
        if directions[i][0] == "N":
            currentPosition[1] += 1
            time += 1
        elif directions[i][0] == "S":
            currentPosition[1] -= 1
            time += 1
        elif directions[i][0] == "W":
            currentPosition[0] -= 1
            time += 1
        elif directions[i][0] == "E":
            currentPosition[0] += 1
            time += 1
        positionAndTime.append([copy.deepcopy(currentPosition), time])


check = False
values = []
for i in range(len(positionAndTime)):
    for j in range(i+1, len(positionAndTime)):
        if positionAndTime[j][0][0] == positionAndTime[i][0][0] and positionAndTime[j][0][1] == positionAndTime[i][0][1]:
            check = True
            values.append(abs(positionAndTime[i][1]-positionAndTime[j][1]))
if check is False:
    print (-1)
else:
    print (min(values))
