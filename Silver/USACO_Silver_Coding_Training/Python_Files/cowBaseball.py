numCows = int(input())
locations = []
for i in range(numCows):
    locations.append(int(input()))
locations.sort()

locations.append(10000000000000000000000000000000000000)


def binarySearch(x):
    start = 0
    end = numCows
    while start < end:
        mid = (start + end) // 2
        if locations[mid] < x:
            start = mid + 1
        else:
            end = mid
    return end


# [        1         3       4         7        10            ]


def checkRange(first, last):
    return binarySearch(last + 1) - binarySearch(first)


count = 0
for i in range(len(locations)):
    for j in range(i + 1, len(locations)):
        low = (locations[j] - locations[i]) + locations[j]
        high = ((locations[j] - locations[i]) * 2) + locations[j]
        count += checkRange(low, high)
print(count)
# print(binarySearch(3))
# [        1         3       4         7        10            ]
