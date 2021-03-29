
numCows = int(input())
cowLineup = []
check = []
for i in range (numCows):
    a = int(input())
    cowLineup.append(a)
    check.append(a)
swapCount = 0
check.sort()
#print (cowLineup)
#print (check)
count = 0
for i in range (numCows):
    if cowLineup[i] != check[i]:
        count +=1
print (count-1)
