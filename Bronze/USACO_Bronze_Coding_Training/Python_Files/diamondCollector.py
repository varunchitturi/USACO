x,y = input().split()
numberOfDiamonds = int(x)
maxDifference = int(y)
diamondSizes = []
for i in range (0,numberOfDiamonds):
    a = input()
    diamondSizes.append(int(a))
diamondSizes.sort()
h = 0
c = 0
for i in range (numberOfDiamonds):
    c = 0
    for j in range (i+1,numberOfDiamonds):
        if diamondSizes[i] + maxDifference >= diamondSizes[j]:
            c+=1
        else:
            break
    if c > h:
        h = c
print (h + 1)
