x,y = input().split()
numCows = int(x)
costumeSize = int(y)
cowSizes = []
#print(numCows)
for i in range(numCows):
    cowSizes.append(int(input()))
total = 0
cowSizes.sort()
for i in range(numCows):
    # now we binary search
    search = costumeSize-cowSizes[i]
    numToGo = 0
    left = i
    right = numCows-1
    if search > cowSizes[i]:
        while(left <= right):
            mid = (left+right)//2
            if left+1 == right or left == right:
                if cowSizes[right] <= search:
                    numToGo = right-i
                    break
                elif cowSizes[left] <= search:
                    numToGo = left-i
                    break
                else:
                    numToGo = -1
                    break

            if cowSizes[mid] <= search:
                left = mid
            else:
                right = mid
        #    print(left, right)
    if numToGo > 0:
        total+=numToGo
#    print(numToGo)
#    print(total)
print(total)
