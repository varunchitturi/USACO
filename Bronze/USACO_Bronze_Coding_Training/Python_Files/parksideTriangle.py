
x,y = input().split()
rows = int(x)
start = int(y)
struct = []
for i in range (rows):
    append1 = []
    for j in range (rows):
        append1.append(' ')
    struct.append(append1)
returnx = 1

for i in range (rows):
    for j in range (returnx):
        if start == 10:
            start = 1
        struct[j][i] = start
        start += 1
    returnx += 1










# printing



for i in range (len(struct)):


    print (*struct[i],sep = ' ')
