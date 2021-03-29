
x,y = input().split()
numberOfCows = int(x)
lengthOfCount = int(y)
sequence = input().split()
lineOfCows = []

currentIndex = 0
for i in range (len(sequence)):
    sequence[i] = int(sequence[i])
for i in range (numberOfCows):
    lineOfCows.append(i+1)
for i in range (len(lineOfCows)):
    lineOfCows[i] = int(lineOfCows[i])
#print (lineOfCows)
#print (sequence)
while len(lineOfCows) > 1:
    for i in range (len(sequence)):
        if len(lineOfCows) > 1:
            currentIndex += sequence[i]-1
            if currentIndex >= (len(lineOfCows)-1):
                currentIndex = (currentIndex % len(lineOfCows))

            del lineOfCows[currentIndex]


print (lineOfCows[0])
