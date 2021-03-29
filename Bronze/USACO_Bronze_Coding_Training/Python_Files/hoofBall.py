
#truncate from a point to the end
def truncateList(list,index):
    truncatedList = []
    for i in range(index,len(list)):
        truncatedList.append(list[i])
    return truncatedList
numCows = int(input())
cowLocations = []
x = input().split()
for i in range (len(x)):
    cowLocations.append(int(x[i]))
cowLocations.sort()
checkIfTouched = [0]*numCows
ballsIntroduced = 0
#print (cowLocations)
#print (checkIfTouched)
def passToCow(index):
    left = -1
    leftDistance = 9999999999999999
    right = -1
    rightDistance = 999999999999999
    for i in range (numCows):
        if cowLocations[i] < cowLocations[index] and cowLocations[index] - cowLocations[i] < leftDistance:
            left = i
            leftDistance = cowLocations[index] - cowLocations[i]
    for i in range (numCows):
        if cowLocations[i] > cowLocations[index] and cowLocations[i] - cowLocations[index] < rightDistance:
            right = i
            rightDistance = cowLocations[i] - cowLocations[index]
    if leftDistance <= rightDistance:
        return left
    else:
        return right
for i in range(numCows):
    checkIfTouched[passToCow(i)] += 1
for i in range (numCows):
    if checkIfTouched[i] == 0:
        ballsIntroduced += 1
    if passToCow(i) > i == passToCow(passToCow(i)) and checkIfTouched[i] == 1 and checkIfTouched[passToCow(i)] == 1:
        ballsIntroduced+=1
print (ballsIntroduced)
