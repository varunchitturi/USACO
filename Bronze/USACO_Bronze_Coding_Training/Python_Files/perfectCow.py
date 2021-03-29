import statistics
inputs = int(input())
cows = []
medians = []
for i in range (inputs):
    x = input().split()
    for j in range (len(x)):
        x[j] = int(x[j])
    cows.append(x)
for i in range (inputs):
    medians.append(statistics.median(cows[i]))
print (statistics.median(medians))
