N, a, b, c, d, e, f, g, h, M = input().split()
N = int(N)
a = int(a)
b = int(b)
c = int(c)
d = int(d)
e = int(e)
f = int(f)
g = int(g)
h = int(h)
M = int(M)
def getWeight(i):
    return (a*i**5+b*i**2+c) % d
def getUtility(i):
    return (e*i**5+f*i**3+g) % h

cows = []
for i in range(N*3):
    cows.append([getUtility(i),getWeight(i)])

def compare(x,y):
        if x[0] > y[0]:
            return -1
        if x[0] < y[0]:
            return 1
        if x[0] == y[0]:
            if x[1] <= y[1]:
                return -1
            else:
                return 1
def cmp_to_key(mycmp):
    'Convert a cmp= function into a key= function'
    class K(object):
        def __init__(self, obj, *args):
            self.obj = obj
        def __lt__(self, other):
            return mycmp(self.obj, other.obj) < 0
        def __gt__(self, other):
            return mycmp(self.obj, other.obj) > 0
        def __eq__(self, other):
            return mycmp(self.obj, other.obj) == 0
        def __le__(self, other):
            return mycmp(self.obj, other.obj) <= 0
        def __ge__(self, other):
            return mycmp(self.obj, other.obj) >= 0
        def __ne__(self, other):
            return mycmp(self.obj, other.obj) != 0
    return K
cows = sorted(cows, key=cmp_to_key(compare))

sum = 0
for i in range(N):
    sum += cows[i][1]

print(sum % M)
print(cows)
