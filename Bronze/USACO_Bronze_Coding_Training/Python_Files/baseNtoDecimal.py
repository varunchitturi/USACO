def baseToDecimal(number,base):
    number = [int(a) for a in str(number)]
    decimal = 0
    for i in range (len(number)):
        decimal += base**(len(number)-1-i)*number[i]
    return decimal
x,y = input().split()
number = int(x)
base = int(y)
print (baseToDecimal(number,base))
