startNumber = input()
check = True
numbers = []
# number = list(startNumber)
numbers.append(int(startNumber))
# numbers.append((int(number[1]+number[2]))**2)
i = 0
while check is True:
    currentNum = numbers[-1]
    if len(str(currentNum)) == 4:
        middleNumSquared = (int((str(currentNum))[1] + (str(currentNum))[2])) * (int((str(currentNum))[1] + (str(currentNum))[2]))
    elif len(str(currentNum)) == 3:
        middleNumSquared = (int((str(currentNum))[0] + (str(currentNum))[1])) * (int((str(currentNum))[0] + (str(currentNum))[1]))
    elif len(str(currentNum)) == 2:
        middleNumSquared = (int((str(currentNum))[0])) * (int((str(currentNum))[0]))
    elif len(str(currentNum)) == 1:
        middleNumSquared = 0
    if middleNumSquared in numbers:
        check = False
    if middleNumSquared not in numbers:
        numbers.append(middleNumSquared)
    # print (numbers)
    # print (currentNum)
    # print (len(str(currentNum)))
    # print (((int((str(currentNum))[0]))) * ((int((str(currentNum))[0]))))
    # print (middleNumSquared)
    i += 1
# print (numbers)
print(len(numbers))
