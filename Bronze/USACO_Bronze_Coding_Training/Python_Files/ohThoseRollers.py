def distance(x1,y1,x2,y2):
    final = 0
    final = ((abs(x1-x2))**2 + (abs(y1-y2))**2)**0.5
    return final
def sorting(numbers_array):
    return sorted(numbers_array, key=abs)
numCoordinates = int(input())
circles = []
for i in range (numCoordinates):
    set = []
    x,y,z = input().split()
    xCoordinate = int(x)
    yCoordinate = int(y)
    radius = int(z)
    number = i
    set = [xCoordinate,yCoordinate,radius]
    circles.append(set)
#print(circles)
totals = []
for i in range (numCoordinates):
    matches = 0
    for j in range (numCoordinates):
        circle1 = circles[i]
        circle2 = circles[j]
        if distance(circle1[0],circle1[1],circle2[0],circle2[1]) == circle1[2] + circle2[2]:
            matches += 1
    if matches == 1:
        totals.append(circle1)
#print (totals)
if totals[0][0] == 0 and totals[0][1] == 0:
    print (totals[1][0],end=" ")
    print (totals[1][1],end=" ")
else:
    print (totals[0][0],end=" ")
    print (totals[0][1],end=" ")
