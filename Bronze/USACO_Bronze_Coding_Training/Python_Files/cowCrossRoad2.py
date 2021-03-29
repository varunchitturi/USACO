def stringToNum(string):
    if string == "A":
        return 1
    if string == "B":
        return 2
    if string == "C":
        return 3
    if string == "D":
        return 4
    if string == "E":
        return 5
    if string == "F":
        return 6
    if string == "G":
        return 7
    if string == "H":
        return 8
    if string == "I":
        return 9
    if string == "J":
        return 10
    if string == "K":
        return 11
    if string == "L":
        return 12
    if string == "M":
        return 13
    if string == "N":
        return 14
    if string == "O":
        return 15
    if string == "P":
        return 16
    if string == "Q":
        return 17
    if string == "R":
        return 18
    if string == "S":
        return 19
    if string == "T":
        return 20
    if string == "U":
        return 21
    if string == "V":
        return 22
    if string == "W":
        return 23
    if string == "X":
        return 24
    if string == "Y":
        return 25
    if string == "Z":
        return 26
def numToString(num):
    if num == 1:
        return "A"
    if num == 2:
        return "B"
    if num == 3:
        return "C"
    if num == 4:
        return "D"
    if num == 5:
        return "E"
    if num == 6:
        return "F"
    if num == 7 :
        return "G"
    if num == 8:
        return "H"
    if num == 9:
        return "I"
    if num == 10:
        return "J"
    if num == 11:
        return "K"
    if num == 12:
        return "L"
    if num == 13:
        return "M"
    if num == 14:
        return "N"
    if num == 15:
        return "O"
    if num == 16:
        return "P"
    if num == 17:
        return "Q"
    if num == 18:
        return "R"
    if num == 19:
        return "S"
    if num == 20:
        return "T"
    if num == 21:
        return "U"
    if num == 22:
        return "V"
    if num == 23:
        return "W"
    if num == 24:
        return "X"
    if num == 25:
        return "Y"
    if num == 26:
        return "Z"
def findLocations(string,list):
    locations = []
    for i in range (len(list)):
        if list[i] == string:
            locations.append(i)
    return locations
def truncateList(list,index):
    truncatedList = []
    for i in range(index,len(list)):
        truncatedList.append(list[i])
    return truncatedList
def truncateListWithEnd(list,index,endIndex):
    truncatedList = []
    for i in range(index,endIndex+1):
        truncatedList.append(list[i])
    return truncatedList
crossingPairs = 0
farm = list(input())

for i in range (0,53):
    if i != 52:
        if farm[i] in truncateList(farm,i+1):
            #print(farm[i+1 : len(farm)-i+1])
            #print (["true",i,numToString(i+1)])
            startIndex = i
            for j in range (i+1,len(farm)):
                if farm[j] == farm[i]:
                    break
            stopIndex = j
            for k in range (startIndex+1,stopIndex):
                if farm[k] in truncateList(farm,stopIndex):
                    crossingPairs += 1
print (crossingPairs)
