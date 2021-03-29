x,y = input().split()
startNumber = int(x)
endNumber = int(y)
numbers = []
for i in range (startNumber,endNumber+1):
    numbers.append(i)
bigNumber = ""
for i in range (0,len(numbers)):
    bigNumber += str(numbers[i])


arrayDigits = [int(d) for d in str(bigNumber)]

num1 = arrayDigits.count(1)
num2 = arrayDigits.count(2)
num3 =arrayDigits.count(3)
num4 =arrayDigits.count(4)
num5 =arrayDigits.count(5)
num6 =arrayDigits.count(6)
num7 =arrayDigits.count(7)
num8 =arrayDigits.count(8)
num9 =arrayDigits.count(9)
num0 =arrayDigits.count(0)

print (num0,end=" ")
print (num1,end=" ")
print (num2,end=" ")
print (num3,end=" ")
print (num4,end=" ")
print (num5,end=" ")
print (num6,end=" ")
print (num7,end=" ")
print (num8,end=" ")
print (num9,end=" ")
