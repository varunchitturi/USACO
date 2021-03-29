x,y = input().split()
slots = int(x)
typesOfFlowers = int(y)
flowerBed = []
startPosition = []
repititonRate = []
for i in range (slots):
    flowerBed.append(1)
for i in range (typesOfFlowers):
    x,y = input().split()
    startPosition.append(int(x))
    repititonRate.append(int(y))
for i in range (typesOfFlowers):
    start = startPosition[i]-1
    rate = repititonRate[i]
    for j in range (start,len(flowerBed)):
        if j == start or(j-start)%rate == 0:
            flowerBed[j] = 0
    #print (flowerBed)
    #print (rate)
    #print(start)
print (sum(flowerBed))
