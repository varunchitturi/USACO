def sorting(numbers_array):
    return sorted(numbers_array, key=abs)
x,y = input().split()
minutesRemaining = int(x)
landmarks = int(y)
landMarkDist = []
for i in range (landmarks):
    a = int(input())
    landMarkDist.append(a)
landMarkDist = sorting(landMarkDist)

timeLapsed = 0
landMarksVisited = 0

timeLapsed += abs(landMarkDist[0])
landMarksVisited += 1
#if landMarkDist[1] > 0 and landMarkDist[0]<0 or landMarkDist[1] < 0 and landMarkDist[0]>0:
    #timeLapsed+=abs(landMarkDist[0])

for i in range (1,landmarks):
    if abs(landMarkDist[i]-landMarkDist[i-1]) + timeLapsed > minutesRemaining:

        break


    else:
        if (landMarkDist[i] > 0 and landMarkDist[i-1] > 0) or (landMarkDist[i] < 0 and landMarkDist[i-1] < 0):
            timeLapsed += abs(landMarkDist[i]-landMarkDist[i-1])
            landMarksVisited+=1

            #print(landMarksVisited)
        else:
            timeLapsed += abs(landMarkDist[i-1])
            timeLapsed += abs(landMarkDist[i])
            landMarksVisited+=1

            #print(landMarksVisited)


print (i)
