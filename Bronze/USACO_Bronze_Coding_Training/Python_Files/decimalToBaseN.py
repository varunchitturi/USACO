def decimalToBase(decimal,base):
    number = []

    while decimal > 0:
        number.append(decimal % base)
        decimal = decimal//base
    number.reverse()
    number = [str(a) for a in number]
    number = "".join(number)
    return int(number)
x,y = input().split()
decimal = int(x)
base = int(y)
print (decimalToBase(decimal,base))
