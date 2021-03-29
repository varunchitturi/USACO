numCows = int(input())
coordinates = []
for i in range(numCows):
    x, y = input().split()
    coordinates.append([int(x), int(y), True])


def findDistance(x1, y1, x2, y2):
    xDist = abs(x1-x2)
    yDist = abs(y1-y2)
    return ((xDist**2)+(yDist**2))


def countAlive():
    counter = 0
    for i in range(numCows):
        if coordinates[i][2] is True:
            counter += 1
    return counter


i = 0
while True:
    if countAlive() == 1:
        break
    if coordinates[i][2] is True:
        x = coordinates[i][0]
        y = coordinates[i][1]
        dist = 9999999999999999999
        index = 0
        for j in range(numCows):
            if findDistance(x, y, coordinates[j][0], coordinates[j][1]) < dist and j != i and coordinates[j][2] is True:
                index = j
                dist = findDistance(x, y, coordinates[j][0], coordinates[j][1])
        coordinates[index][2] = False
    #print(coordinates)
    if i == numCows - 1:
        i = 0
    else:
        i += 1
for i in range(numCows):
    if coordinates[i][2] is True:
        print(i+1)
        break
