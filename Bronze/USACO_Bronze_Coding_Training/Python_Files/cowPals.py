import math
#this is way slower
def divisorSum(num):
    divisors = []
    for i in range (1,num):
        if num % i == 0:
            divisors.append(i)

    return sum(divisors)

def divisorSum2(num):
    divisors = 0
    for i in range (1,int(math.sqrt(num))+1):
        if num % i == 0:
            divisors+=i
            divisors+=(int(num/i))
    divisors-=num;
    return divisors

startInteger = int(input())
num = 1

while True:
    i = startInteger + num
    k = divisorSum2(i)
    if divisorSum2(k)== i:
        if i == k:
            num+=1
        else:
            break
    else:
        num+=1

print(i,end=" ")
print(k,end=" ")
