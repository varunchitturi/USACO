numNotes = int(input())
notes = []


def getDifferences(array):
    differenceArray = []
    for i in range(len(array)-1):
        differenceArray.append(array[i]-array[i+1])
    return differenceArray


for i in range(numNotes):
    notes.append(int(input()))
numRuminantNotes = int(input())
ruminantNotes = []
for i in range(numRuminantNotes):
    ruminantNotes.append(int(input()))
ruminantNotes.sort()
differenceArray = getDifferences(ruminantNotes)
final = []
for i in range(len(notes)-numRuminantNotes+1):
    array = []
    for j in range(len(ruminantNotes)):
        array.append(notes[i+j])
    array.sort()
    diffArray = getDifferences(array)
    # print(array)
    # print(diffArray)
    if differenceArray == diffArray:
        final.append(i+1)

# print(final)
print(len(final))
for i in range(len(final)):
    print(final[i])
