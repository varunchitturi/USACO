numHills = int(input())
hills = []
vals = []

for i in range(numHills):
    x = int(input())
    hills.append(x)
hills.sort()
for i in range(83):
    count = 0
    for j in range(numHills):
        if hills[j] > i + 17:
            count += ((hills[j]-(i+17))**2)
        elif hills[j] < i:
            count += ((i-hills[j])**2)
    vals.append(count)
print(min(vals))
