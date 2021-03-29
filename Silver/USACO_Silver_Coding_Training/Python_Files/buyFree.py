x,y = input().split()
numGoodQuality = int(x)
numBadQuality = int(y)
goodQuality = []
badQuality = []
for i in range(numGoodQuality):
    goodQuality.append(int(input()))
for i in range(numBadQuality):
    badQuality.append(int(input()))
goodQuality.sort(reverse=True)
badQuality.sort(reverse=True)
maxNum = numGoodQuality
for i in range(numGoodQuality):
    for j in range(len(badQuality)):
        if goodQuality[i] > badQuality[j]:
            maxNum += 1
            del badQuality[j]
            break

print(maxNum)
