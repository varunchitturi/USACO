x,y = input().split()
farmer = int(x)
bessie = int(y)
farmerinitial = int(x)
bessieinitial = int(y)
i = 1
total = 0

if farmerinitial<bessieinitial:
    while True:
        farmer += i
        if farmer >= bessie:
            total += i - (farmer-bessie)
            break
        #print (farmer)
        #print(total)
        #print (i)
        farmer -= i
        if farmer >= bessie:
            total += i - (farmer-bessie)
            break
        total += abs(i)
        total += abs(i)
        i = i*(-2)
else:
    while True:
        farmer += i
        if farmer <= bessie:
            total += abs(i) - (bessie-farmer)
            break
        total += abs(i)
        #print (farmer)
        #print(total)
        #print (i)
        farmer -= i
        if farmer <= bessie:
            total += abs(i) - (bessie-farmer)
            break

        total += abs(i)
        #print (total)
        i = i*(-2)

print (total)
