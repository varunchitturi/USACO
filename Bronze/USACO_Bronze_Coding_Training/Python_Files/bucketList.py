
numCows = int(input())
transcript = []
findMaxTime = []
startTime = []
endTime = []
bucketsNeeded = []
for i in range (numCows):
    toAppend = []
    x,y,z = input().split()
    toAppend= [int(x),int(y),int(z)]
    transcript.append(toAppend)
    findMaxTime.append(int(y))
    startTime.append(int(x))
    endTime.append(int(y))
    bucketsNeeded.append(int(z))
transcript.sort()
findMaxTime = max(findMaxTime)
def findIndexStartTime(startTime):
    for i in range (len(transcript)):
        if transcript[i][0] == startTime:
            return i
def findIndexEndTime(endTime):
    for i in range (len(transcript)):
        if transcript[i][1] == endTime:
            return i
bucketsUsed = 0
bucketsAvailable = 0
processNumber = -1
processGoingOn = 0
start = 0
end = 0
total = []
for currentTime in range (transcript[0][0],findMaxTime):
    if currentTime in endTime:
        processGoingOn -= 1
        bucketsUsed -= bucketsNeeded[endTime.index(currentTime)]
        total.append(bucketsUsed)
    if processGoingOn == 0 and currentTime in startTime:
        processGoingOn += 1
        bucketsUsed = bucketsNeeded[startTime.index(currentTime)]
        total.append(bucketsUsed)
    elif processGoingOn > 0 and currentTime in startTime:
        processGoingOn += 1
        bucketsUsed += bucketsNeeded[startTime.index(currentTime)]
        total.append(bucketsUsed)
print (max(total))
