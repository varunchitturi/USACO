billboard1 = input().split()
billboard2 = input().split()
truck = input().split()
for i in range (len(billboard1)):
    billboard1[i] = int(billboard1[i])
for i in range (len(billboard2)):
    billboard2[i] = int(billboard2[i])
for i in range (len(truck)):
    truck[i] = int(truck[i])
minX1 = min(billboard1[0],billboard2[0],truck[0])
maxX2 = max(billboard1[2],billboard2[2],truck[2])
width = maxX2-minX1
minY1 = min(billboard1[1],billboard2[1],truck[1])
maxY2 = max(billboard1[3],billboard2[3],truck[3])
length = maxY2-minY1
totalMatrix = []
smallMatrix = []
for i in range (2000):
    for j in range (2000):
        smallMatrix.append(0)
    totalMatrix.append(smallMatrix)
    smallMatrix = []
for i in range(billboard1[1],billboard1[3]):
    for j in range (billboard1[0],billboard1[2]):
        totalMatrix[j+minY1][i+minX1] = 1


for i in range(billboard2[1],billboard2[3]):
    for j in range (billboard2[0],billboard2[2]):
        totalMatrix[j+minY1][i+minX1] = 1

for i in range(truck[1],truck[3]):
    for j in range (truck[0],truck[2]):
        totalMatrix[j+minY1][i+minX1] = 0

hi = 0
for i in range (len(totalMatrix)):
    hi += sum(totalMatrix[i])
print (hi)
