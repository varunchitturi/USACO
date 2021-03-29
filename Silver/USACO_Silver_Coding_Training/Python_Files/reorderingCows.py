import copy
numCows = int(input())
initialOrder = []
finalOrder = []
for i in range(numCows):
    initialOrder.append(int(input()))
for i in range(numCows):
    finalOrder.append(int(input()))

done = []
sets = []
greatestSize = 0
for i in range(len(initialOrder)):
    if initialOrder[i] not in done:
        temp = copy.deepcopy(initialOrder)
        encountered = []
        current = i
        encountered.append(temp[current])
        temp[i] = -1
        while True:
            temp[current] = -1
            current = finalOrder.index(encountered[-1])
            if temp[current] == -1:
                break
            else:
                encountered.append(temp[current])
        if len(encountered) > 1:
            sets.append(encountered)
        for i in range(len(encountered)):
            done.append(encountered[i])
        if len(encountered) > greatestSize:
            greatestSize = len(encountered)
if len(sets) > 0:
    print(str(len(sets)) + " " + str(greatestSize))
else:
    print("0 -1")
#print(sets)