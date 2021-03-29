import copy
numLifegaurds = int(input())
timesOfGaurds = [] # hours of each life gaurd
timesOfGaurdsReset = []
greatestTime = [] # the time when pool closes
times = [] # range of pool times
maxTimes = [] #the greatest amounts of times that life gaurds will be available
for i in range (numLifegaurds):
    x,y = input().split()
    timesOfGaurds.append([int(x),int(y)])
    timesOfGaurdsReset.append([int(x),int(y)])
for i in range (numLifegaurds):
    greatestTime.append(timesOfGaurds[i][1])
greatestTime.sort(reverse = True)
greatestTime = greatestTime[0]
for i in range (greatestTime+2):
    times.append(0)
timesReset = copy.deepcopy(times)
for i in range(numLifegaurds):

    del timesOfGaurds[i]
    for j in range (numLifegaurds-1):
        for k in range (timesOfGaurds[j][0],timesOfGaurds[j][1]):
            times[k] = 1

    maxTimes.append(sum(times))
    timesOfGaurds = copy.deepcopy(timesOfGaurdsReset)
    times = copy.deepcopy(timesReset)
print(max(maxTimes))
