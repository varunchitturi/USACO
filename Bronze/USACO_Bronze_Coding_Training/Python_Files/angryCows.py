#truncate from a point to the end
def truncateList(list,index):
    truncatedList = []
    for i in range(index,len(list)):
        truncatedList.append(list[i])
    return truncatedList
#truncate from a point to another point
def truncateListWithEnd(list,index,endIndex):
    truncatedList = []
    for i in range(index,endIndex+1):
        truncatedList.append(list[i])
    return truncatedList


numBales = int(input())
balePosition = []
for i in range (numBales):
    balePosition.append(int(input()))
balePosition.sort()


allExplosion = []
for i in range (numBales):
    currentBale = balePosition[i]
    explosionRadius = 1
    baleExplosions = 1
    if i == 0:
        check = currentBale + explosionRadius
        while currentBale < balePosition[-1] and currentBale + explosionRadius >= balePosition [balePosition.index(currentBale)+1]:

            while True:
                if check in balePosition:
                    baleExplosions += balePosition.index(check) - balePosition.index(currentBale)
                    currentBale = check
                    explosionRadius += 1
                    check = currentBale + explosionRadius
                    #print ("----------------")
                    #print (currentBale)
                    #print (check)
                    #print (baleExplosions)
                    #print ("------------------")

                    break
                if check == currentBale :
                    break
                else:
                    check = check - 1
        allExplosion.append(baleExplosions)

    elif i != 0 and i != numBales-1:
        #forward
        check = currentBale + explosionRadius
        while currentBale < balePosition[-1] and (currentBale + explosionRadius) >= balePosition[balePosition.index(currentBale)+1]:

            while True:
                if check in balePosition:
                    baleExplosions += balePosition.index(check) - balePosition.index(currentBale)
                    currentBale = check
                    explosionRadius += 1
                    check = currentBale + explosionRadius
                    break
                if check == currentBale:
                    break
                else:
                    check = check -1
        #backward
        currentBale = balePosition[i]
        explosionRadius = 1
        while currentBale > balePosition[0] and currentBale - explosionRadius <= balePosition[balePosition.index(currentBale)-1]:
            check = currentBale - explosionRadius
            while True:
                if check in balePosition:
                    baleExplosions += balePosition.index(currentBale) - balePosition.index(check)
                    currentBale = check
                    explosionRadius += 1
                    check = currentBale - explosionRadius
                    break
                if check == currentBale:
                    break
                else:
                    check = check + 1

        allExplosion.append(baleExplosions)
    elif i == numBales-1:
        while currentBale > balePosition[0] and currentBale - explosionRadius <= balePosition[balePosition.index(currentBale)-1]:
            check = currentBale - explosionRadius
            while True:
                if check in balePosition:
                    baleExplosions += balePosition.index(currentBale)- balePosition.index(check)
                    currentBale = check
                    explosionRadius += 1
                    check = currentBale - explosionRadius
                    break
                if check == currentBale:
                    break
                else:
                    check = check + 1
        allExplosion.append(baleExplosions)
print (max(allExplosion))
