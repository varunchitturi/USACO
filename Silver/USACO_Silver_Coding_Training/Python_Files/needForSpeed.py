a,b,c = input().split()
mass = int(b)
force = int(a)
numPieces = int(c)
pieces = []
answer = []
ratio = force/ mass
for i in range(numPieces):
    x,y = input().split()
    forcep = int(x)
    massp = int(y)
    pieces.append([forcep/massp, forcep, massp, i+1])
pieces.sort(reverse=True)
for i in range(len(pieces)):
    if pieces[i][0] < ratio:
        break
    else:
        answer.append(pieces[i][3])
        force += pieces[i][1]
        mass += pieces[i][2]
        ratio = force/mass
if (len(answer) == 0):
    print("NONE")
else:
    answer.sort()
    for i in range(len(answer)):
        print(answer[i])
