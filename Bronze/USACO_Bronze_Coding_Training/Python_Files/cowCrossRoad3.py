numCows = int(input())
cowTimings = [] #arrival , questioning time
totalTime = 0
for i in range (numCows):
    x,y = input().split()
    cowTimings.append([int(x),int(y)])
cowTimings.sort()
#print (cowTimings)
for i in range (numCows):
    if i == 0:
        totalTime += cowTimings[i][0]
        totalTime += cowTimings[i][1]
    if i != 0:
        if totalTime >= cowTimings[i][0]:
            totalTime += cowTimings[i][1]
        else:
            totalTime += cowTimings[i][0]-totalTime
            totalTime += cowTimings[i][1]

print (totalTime)
