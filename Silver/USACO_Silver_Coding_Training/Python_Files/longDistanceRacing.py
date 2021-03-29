a,b,c,d,e = input().split()
timeLimit = int(a)
numSegments = int(b)
upHillTime = int(c)
flatTime = int(d)
downHillTime = int(e)
segments = []
length = 0
for i in range(numSegments):
    x = input()
    if x == 'f':
        segments.append(2*flatTime)
    elif x == 'u' or x == 'd':
        segments.append(upHillTime+downHillTime)

time = 0
for i in range(numSegments):
    if segments[i] + time > timeLimit:
        break
    else:
        length += 1
        time += segments[i]
print(length)