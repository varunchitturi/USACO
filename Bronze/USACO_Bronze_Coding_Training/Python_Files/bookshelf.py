x,y = input().split()
numberOfCows = int(x)
sumHeight = int(y)
heights = []
for i in range (numberOfCows):
    a = int(input())
    heights.append(a)
heights.sort(reverse=True)
finalArr =[]
i = 0
while True:
    if sum(finalArr) == sumHeight:
        break
    elif sum(finalArr) > sumHeight:
        break

    elif sum(finalArr) < sumHeight:
        finalArr.append(heights[i])


    i+=1
print (len(finalArr))
