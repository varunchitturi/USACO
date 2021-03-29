x,y,z = input().split()
length = int(x)
width = int(y)
scale = int(z)
lines = []
for i in range (0,length):
    a = input()
    lines.append(a)

for i in range (0,length):
    splitLine = (list(lines[i]))
    printAr = []
    for j in range (0,width):
        for k in range(0,scale):
            printAr.append(splitLine[j])
    for l in range(0,scale):
        print (str("".join(printAr)))
