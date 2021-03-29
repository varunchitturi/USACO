import copy
x, y = input().split()
numKnots = int(x)
length = int(y)
knotLocations = []
for i in range(numKnots):
    knotLocations.append(int(input()))
knotLocations.sort()
if numKnots % 2 == 0:
    halfway = int((knotLocations[int(numKnots/2-1)] + knotLocations[int(numKnots/2)])/2)
else:
    halfway = knotLocations[numKnots//2]
count = 0

# print(knotLocations)
# print(halfway)


def check(c, a):
    array = copy.deepcopy(c)
    firstSingular = 809990854
    if a == array[0]:
        del array[0]
    # print(len(array)//2)
    for i in range(0, (len(array)//2)+1, 2):
        if array[i] != array[i+1]:
            firstSingular = i
            break
    for i in range(len(array)-1, 0, -1):
        if array[i] == array[i-1]:
            firstDouble = i
            break
    if firstSingular == 809990854:
        return True
    if firstDouble > firstSingular:
        return False
    if firstDouble < firstSingular:
        return True


def fold(location):
    passed = 0
    knot = copy.deepcopy(knotLocations)
    for i in range(numKnots):
        if knot[i] < location:
            knot[i] = abs(location - knot[i]) + location
            passed += 1
        else:
            break
    knot.sort()
    for i in range(len(knot)):
        if knot[i] % 1 == 0:
            knot[i] = int(knot[i])
    # print(knot)
    if location < halfway:
        if len(list(set(knot))) == numKnots - passed and check(knot, location) is True:
            # print(True)
            return True
        else:
            return False
    elif location > halfway:
        if location == knot[0]:
            del knot[0]
        if len(list(set(knot))) == passed and check(knot, location) is True:
            # print(True)
            return True
        else:
            return False
    elif location == halfway:
        if location == knot[0]:
            del knot[0]
        if len(list(set(knot))) == int(numKnots/2) and check(knot, location) is True:
            # print(True)
            return True
        else:
            return False


i = min(knotLocations) + 0.5

while i < max(knotLocations):
    # print(i)
    if fold(i) is True:
        count += 1
    i += 0.5

print(count)
# print(check([6, 6, 8, 10, 10], 5))
