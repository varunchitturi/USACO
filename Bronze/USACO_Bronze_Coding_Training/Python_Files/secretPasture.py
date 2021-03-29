import math
def maxInteger(num):
    while True:
        if math.sqrt(num) == int(math.sqrt(num)):
            maxInteger = math.sqrt(num)
            return int(maxInteger)
            break
        else:
            num -= 1


size = int(input())
a = int(math.floor(math.sqrt(size)))+1




ways = 0
for i in range (0,a):
    for j in range (0,a):
        for k in range (0,a):
            diff = size-(i*i+j*j+k*k)
            if diff >= 0:
                if math.sqrt(diff) == math.sqrt(diff)//1:

                    ways+= (1)

print (ways)
