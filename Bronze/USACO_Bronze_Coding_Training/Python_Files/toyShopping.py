toysAvailable = int(input())
joy = []
price = []
happyFrugal = []
totalPrice = 0
index = []
for i in range (toysAvailable):
    x,y = input().split()
    joy.append(int(x))
    price.append(int(y))
    a = int(x)
    b = int(y)
    happyFrugal.append(a/b)
for i in range (0,3):

    x = (happyFrugal.index(max(happyFrugal)))
    happyFrugal[x] = 0

    totalPrice += price[x]
    index.append(x)
    i = 0
print (totalPrice)
for i in range (3):
    print (index[i]+1)
