import math

#inputs
numberOfRooms = int(input())
cowsPerRoom = []
for i in range (0,numberOfRooms):
    cows = int(input())
    cowsPerRoom.append(cows)

doorsEntered =[]
#cycle array
def doorCount(array):
    sum = 0
    for i in range(0,numberOfRooms):
        sum += (array[i]*i)
    return sum
lastIndex = numberOfRooms-1
for i in range (0,numberOfRooms):
    lastDigit = cowsPerRoom[lastIndex]
    for j in range (0,numberOfRooms-1):
        cowsPerRoom[lastIndex-j] = cowsPerRoom[lastIndex-j-1]
    cowsPerRoom[0] =lastDigit
    cowsPerRoom = list(map(int, cowsPerRoom))
    doorsEntered.append(doorCount(cowsPerRoom))
print (min(doorsEntered))
