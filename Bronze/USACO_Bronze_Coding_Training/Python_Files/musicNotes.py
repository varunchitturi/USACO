x,y = input().split()
numNotes = int(x)
numQueries = int(y)
lengthOfNote = []
answer = []
#queryLocation = []
for i in range (numNotes):
    if i == 0:
        x = int(input())
        lengthOfNote.append(x)
    else:
        x = int(input())
        lengthOfNote.append(x+lengthOfNote[i-1])
for i in range (numQueries):
    queryLocation = int(input())
    #queryLocation.append(x)
    for j in range (len(lengthOfNote)):

        if queryLocation in range (0,lengthOfNote[0]):
            answer.append(1)
            break
        else:
            if queryLocation in range (lengthOfNote[j-1],lengthOfNote[j]):
                answer.append(j+1)
                break
for i in range (len(answer)):
    print (answer[i])
