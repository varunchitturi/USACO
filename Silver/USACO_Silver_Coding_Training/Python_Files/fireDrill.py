numCows = int(input())
cows = []
for i in range(numCows):
    cows.append([i,0])
cows[0] = -1
def rotate(start, toUse):
    #if cows[start] != -1:
     #   cows[start][1] += 1

    currentCow = toUse
    replacedCow = cows[(start+currentCow[0]+1)%len(cows)]
    if replacedCow == -1:
        print(currentCow[0] + 1)
        return 0
    replacedCow[1] += 1
    if(replacedCow[1] > 1):
        print(currentCow[0] + 1)
        return 0
    else:
        final = replacedCow[0]
        cows[(start+currentCow[0]+1)%len(cows)] = currentCow
        rotate((start + start+1)%len(cows),replacedCow)
rotate(0,[0,1])

