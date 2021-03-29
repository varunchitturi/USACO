def flip90(list):
    columns = []

    for i in range(len(list[0])):
        singleColumn = []
        for j in range(len(list)-1, -1, -1):
            singleColumn.append(list[j][i])
        columns.append(singleColumn)
    return (columns)


def reflect(list):
    reflected = []
    for i in range(len(list)):
        row = []
        for j in range(len(list)-1, -1, -1):
            row.append(list[i][j])
        reflected.append(row)
    return (reflected)


size = int(input())
original = []
transformed = []
for i in range(size):
    x = list(input())
    original.append(x)
for i in range(size):
    x = list(input())
    transformed.append(x)

if transformed == flip90(original):
    print (1)
elif transformed == flip90(flip90(original)):
    print (2)
elif transformed == flip90(flip90(flip90(original))):
    print (3)
elif transformed == flip90(reflect(original)) or transformed == flip90(flip90(reflect(original))) or transformed == flip90(flip90(flip90(reflect(original)))):
    print (5)
elif original == transformed:
    print (6)
else:
    print (7)
