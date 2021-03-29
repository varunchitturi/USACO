n, q = [int(x) for x in input().split()]
toSearch = []
if n != 0:
    toSearch = [int(x) for x in input().split()]
query = [0]*q
toSearch.append(-1)
for i in range(q):
    query[i] = int(input())

for i in range(q):
    search = query[i]
    l = 0
    r = n
    while(l <= r):
        m = int((l+r)/2)
        if l == r or l+1 == r:
            if toSearch[l] == search:
                print (l)
                var1 = 0;
                break
            if toSearch[r] == search:
                print (r)
                var2 = 0
                break
            else:
                print(-1)
                break
        if toSearch[m] >= search:
            r = m
        else:
            l = m
