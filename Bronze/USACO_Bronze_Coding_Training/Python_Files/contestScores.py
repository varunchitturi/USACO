numScores = int(input())
scoreList = [int(x) for x in input().split()]
newList = []
newList.append(scoreList[0])
counter = 0
for i in range (1,numScores):

    a = max(newList)
    b = min(newList)
    newList.append(scoreList[i])
    if newList[i] > a or newList[i] < b:
        counter += 1
print (counter)
