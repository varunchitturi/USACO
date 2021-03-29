numCows = int(input())
cows = []
toGo = []
for i in range(numCows):
    toAppend = []
    a = input().split()
    toAppend.append(int(a[0]))
    numTouched = int(a[1])
    touched = []
    for j in range(numTouched):
        touched.append(int(a[j+2]))
    toAppend.append(touched)
    toAppend.append(0)
    toAppend.append(0)
    toAppend.insert(0,1000000000000000000000000000000000000000000000)
    cows.append(toAppend)
    toGo.append(toAppend)
def findFirstIndex():
    minimum = 10000000000000000000000000000
    for i in range(len(toGo)):
        if minimum > toGo[i][0] and toGo[i][4] != 2:
            minimum = toGo[i][0]
            index = i
    return index

current = 0
toGo[0][0] = toGo[0][1]
greatestTime = 0
while True:
    a = findFirstIndex()
    for i in range(len(toGo[a][2])):
        b = toGo[a][2][i]-1
        if toGo[b][4] != 1 and toGo[b][4] != 2:
            toGo[b][3] = toGo[a][0]
            toGo[b][0] = toGo[b][3] + toGo[b][1]
            if greatestTime < toGo[b][0]:
                greatestTime = toGo[b][0]
        if toGo[b][4] ==  0:
            toGo[b][4] = 1
    check = False
    toGo[a][4] = 2
    for i in range(len(toGo)):
        if toGo[i][4] == 0:
            check = True
            break
    if check is False:
        greatestTime = 0
        for i in range(len(toGo)):
            if toGo[i][0] > greatestTime:
                greatestTime = toGo[i][0]
        break

print(greatestTime)



