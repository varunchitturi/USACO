number = list(input())
binary = []
for i in range (len(number)):
    if number[i] == "0":
        binary.append("0000")
    elif number[i] == "1":
        binary.append("0001")
    elif number[i] == "2":
        binary.append("0010")
    elif number[i] == "3":
        binary.append("0011")
    elif number[i] == "4":
        binary.append("0100")
    elif number[i] == '5':
        binary.append("0101")
    elif number[i] == '6':
        binary.append("0110")
    elif number[i] == '7':
        binary.append("0111")
    elif number[i] == '8':
        binary.append("1000")
    elif number[i] == '9':
        binary.append("1001")
    elif number[i] == "A":
        binary.append("1010")
    elif number[i] == "B":
        binary.append("1011")
    elif number[i] == "C":
        binary.append("1100")
    elif number[i] == "D":
        binary.append("1101")
    elif number[i] == "E":
        binary.append("1110")
    elif number[i] == "F":
        binary.append("1111")
#binary = list(binary)
x = "".join(list(binary))
if len(x) % 3 == 2:
    binary.insert(0,"0")
elif len(x) % 3 == 1:
    binary.insert(0,"0")
    binary.insert(0,"0")
binary = "".join(list(binary))
#print(binary)
octal = []
for i in range (0,len(binary)-2,+3):
    toCheck = []
    toCheck.append(binary[i])
    toCheck.append(binary[i+1])
    toCheck.append(binary[i+2])
    i += 3
    toCheck = "".join(toCheck)

    #print (toCheck)
    if toCheck == "000":
        octal.append("0")
    elif toCheck == "001":
        octal.append("1")
    elif toCheck == "010":
        octal.append("2")
    elif toCheck == "011":
        octal.append("3")
    elif toCheck == "100":
        octal.append("4")
    elif toCheck == "101":
        octal.append("5")
    elif toCheck == "110":
        octal.append("6")
    elif toCheck == "111":
        octal.append("7")

octal = "".join(octal)
octal = int(octal)
print(octal)
