x,y = input().split()
numNotes = int(x)
numQueries = int(y)
lengthOfNote = []
query = []
answer = []
#queryLocation = []

for i in range (numNotes):
    if i == 0:
        x = int(input())
        lengthOfNote.append(x)
    else:
        x = int(input())
        lengthOfNote.append(x+lengthOfNote[i-1])
lengthOfNote.insert(0,0)
lengthOfNote.sort()
#print (lengthOfNote)
for i in range(numQueries):
    x = int(input())
    query.append(x)
#print (lengthOfNote)
mid = int(((len(lengthOfNote)-1)/2))
for i in range(len(query)):
    maximum = (len(lengthOfNote))
    while True:
        if query[i] == 0:
            answer.append(1)
            break
        if lengthOfNote[mid] <= query[i]:
            if lengthOfNote[mid+1] > query[i]:
                #print(mid)
                answer.append(mid+1)
                break
            else:
                mid += int((maximum-mid)/2)
        if lengthOfNote[mid] > query[i]:
            maximum = mid
            mid = int(mid/2)
#print (answer)
for i in range (len(answer)):
    print (answer[i])
