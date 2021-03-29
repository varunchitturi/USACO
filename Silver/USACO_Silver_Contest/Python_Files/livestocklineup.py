from itertools import permutations
with open('lineup.in', 'r') as fin:
    a = fin.readline().strip()
    numCommands = int(a)
    commands = []
    for i in range(numCommands):
        a = fin.readline().strip()
        new = a.split(' must be milked beside ')
        commands.append([new[0],new[1]])
#commands = [["Buttercup","Bella"],["Blue","Bella"],["Sue","Beatrice"]]
cows = ["Bessie", "Buttercup", "Belinda", "Beatrice", "Bella", "Blue", "Betsy", "Sue"]
perm = list(permutations(cows))
working = []
print(perm)
for i in range(len(perm)):
    check = True
    perm[i] = list(perm[i])
    for j in range(len(commands)):
        if perm[i].index(commands[j][0]) == 7:
            if perm[i][perm[i].index(commands[j][0]) - 1] != commands[j][1]:
                check = False
                break
        elif perm[i].index(commands[j][0]) == 0:
            if perm[i][perm[i].index(commands[j][0]) + 1] != commands[j][1]:
                check = False
                break
        else:
            if perm[i][perm[i].index(commands[j][0]) + 1] != commands[j][1] and perm[i][perm[i].index(commands[j][0]) - 1] != commands[j][1]:
                check = False
                break
    if check is True:
        working.append(perm[i])
working.sort()
final = working[0]
#print(final)
with open('lineup.out', 'w') as fout:
    for i in range(8):
        fout.write(str(final[i])+ "\n")