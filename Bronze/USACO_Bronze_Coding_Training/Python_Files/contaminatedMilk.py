a,b,c,d = input().split()
peopleAtParty = int(a)
typesOfMilk = int(b)
numberOfLogs = int(c)
numberOfSickLogs = int(d)
milkTranscript = []
for i in range (numberOfLogs):
    a,b,c = input().split()
    milkTranscript.append([int(c),int(b),int(a)])
milkTranscript.sort()
sickTranscript = []
for i in range (numberOfSickLogs):
    a,b = input().split()
    sickTranscript.append([int(b),int(a)])
sickTranscript.sort()
sickIndices = [0]*numberOfSickLogs
for i in range (numberOfSickLogs):
    for j in range (len(milkTranscript)):
        if milkTranscript[j][0] >= sickTranscript[i][0]:
            break
        else:
            sickIndices[i] = [j,sickTranscript[i][1]]
whatEachSickPersonDrank = []
for i in range (len(sickIndices)):
    appendTo = []
    for j in range (numberOfLogs):
        if j <= sickIndices[i][0] and milkTranscript[j][2] == sickIndices[i][1]:
            appendTo.append(milkTranscript[j][1])
        elif j > sickIndices[i][0]:
            break
    whatEachSickPersonDrank.append(appendTo)
possibleMilks = []
check = False
for i in range (len(whatEachSickPersonDrank[0])):
    check = False
    for j in range (len(whatEachSickPersonDrank)):
        if whatEachSickPersonDrank[0][i] in whatEachSickPersonDrank[j]:
            check = True
        else:
            check = False
            break
    if check == True:
        possibleMilks.append(whatEachSickPersonDrank[0][i])
count = []
for i in range (len(possibleMilks)):
    iterator = 0
    peopleGot = []
    for k in range(numberOfLogs):
        if milkTranscript[k][1] == possibleMilks[i] and milkTranscript[k][2] not in peopleGot:
            peopleGot.append(milkTranscript[k][2])
            iterator += 1
    count.append(iterator)
#print (milkTranscript)
#print (whatEachSickPersonDrank)
print (max(count))
#print (sickTranscript)
#print (sickIndices)
