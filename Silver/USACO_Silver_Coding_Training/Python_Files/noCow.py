

x,y = input().split()

numCows = int(x)
k = int(y)
adjectives = []
a = input().split()
finishedAdjectives = []
for i in range(len(a)-5):
    adjectives.append([])

for i in range(numCows):
    if i != 0:
        a = input().split()
    string = ""
    for j in range(4,len(a)-1):
        adjectives[j-4].append(a[j])
        string += a[j]
        string += " "
    finishedAdjectives.append(string)

def combinations(arr):
    # number of arrays
    n = len(arr)


    indices = [0 for i in range(n)]
    stringsArray = []
    while (1):


        string = ""
        for i in range(n):
            string += arr[i][indices[i]]
            string += " "
        stringsArray.append(string)


        next = n - 1
        while (next >= 0 and
               (indices[next] + 1 >= len(arr[next]))):
            next -= 1


        if (next < 0):
            return stringsArray


        indices[next] += 1


        for i in range(next + 1, n):
            indices[i] = 0


final = sorted(list(set(combinations(adjectives))))

final = set(final).difference(set(finishedAdjectives))
final = sorted(list(final))

print(final.rstrip())
