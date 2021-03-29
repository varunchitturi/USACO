x,y = input().split()
numHayBales = int(x)
numQueries = int(y)
a = input()
locations = []
locations = [int(i) for i in a.split()]
locations.sort()
locations.append(99999999999999999999999999)
def binarySearch(x):
    start = 0
    end = numHayBales
    while start < end:
        mid = (start + end) // 2
        if locations[mid] < x:
            start = mid + 1
        else:
            end = mid
    return end
def checkRange(first, last):
    return binarySearch(last +1) - binarySearch(first)
queries = []
for i in range(numQueries):
    x,y = input().split()
    queries.append([int(x),int(y)])
for i in range(len(queries)):
    print(checkRange(queries[i][0],queries[i][1]))
