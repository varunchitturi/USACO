def binaryToDecimal(binary):
    binary = [int(a) for a in str(binary)]
    decimal = 0
    for i in range (len(binary)):
        decimal += 2**(len(binary)-1-i)*binary[i]
    return decimal
def decimalToBinary(decimal):
    binary = []

    while decimal > 0:
        binary.append(decimal % 2)
        decimal = decimal//2
    binary.reverse()
    binary = [str(a) for a in binary]
    binary = "".join(binary)
    return int(binary)

input = int(input())
a = binaryToDecimal(input)
b = a * 17
c = decimalToBinary(b)
print (c)
