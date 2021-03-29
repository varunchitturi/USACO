numVariable = int(input())
varB = []
varE = []
varS = []
varI = []
varG = []
varO = []
varM = []
countEvenB = 0
countOddB = 0
countEvenE = 0
countOddE = 0
countEvenS = 0
countOddS = 0
countEvenI = 0
countOddI = 0
countEvenG = 0
countOddG = 0
countEvenO = 0
countOddO = 0
countEvenM = 0
countOddM = 0
total = 1
for i in range (numVariable):
    x,y = input().split()
    check = [x,int(y)%2]
    if check[0] =="B":
        varB.append(check[1])
        if check[1] ==1:
            countOddB += 1
        else:
            countEvenB += 1
    elif check[0] == "E":
        varE.append(check[1])
        if check[1] ==1:
            countOddB += 1
        else:
            countEvenB += 1
    elif check[0] == "S":
        varS.append(check[1])
        if check[1] ==1:
            countOddB += 1
        else:
            countEvenB += 1
    elif check[0] == "I":
        varI.append(check[1])
        if check[1] ==1:
            countOddB += 1
        else:
            countEvenB += 1
    elif check[0] == "O":
        varG.append(check[1])
        if check[1] ==1:
            countOddB += 1
        else:
            countEvenB += 1
    elif check[0] == "G":
        varO.append(check[1])
        if check[1] ==1:
            countOddB += 1
        else:
            countEvenB += 1
    elif check[0] == "M":
        varM.append(check[1])
        if check[1] ==1:
            countOddB += 1
        else:
            countEvenB += 1
'''varB = list(set(varB))
varE = list(set(varE))
varG = list(set(varG))
varI = list(set(varI))
varM = list(set(varM))
varO = list(set(varO))
varS = list(set(varS))'''
finalAray = ([varB,varE,varG,varI,varM,varO,varS])
possibility = []
for a in range (2):#B
    for b in range (2):#E
        for c in range (2):#G
            for d in range (2):#I
                for e in range (2):#M
                    for f in range (2):#O
                        for g in range (2):#S
                            if ((a+b+g+g+d+b) * (c+f+b+g) * (e+f+f) ) % 2 == 0:
                                possibility.append([a,b,c,d,e,f,g])

count = 0
for i in range (len(possibility)):
    total = 1
    for j in range (7):
        total *= finalAray[j].count(possibility[i][j])
    count += total
print (count)
