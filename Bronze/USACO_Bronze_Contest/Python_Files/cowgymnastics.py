with open('gymnastics.in', 'r') as fin:
    a = fin.readline().strip()
    x,y = a.split()
    numSessions = int(x)
    cows = int(y)
    sessions = []
    for i in range(numSessions):
        a = fin.readline().strip()
        toAppend = a.split()
        sessions.append(toAppend)
for i in range(len(sessions)):
    for j in range(len(sessions[i])):
        sessions[i][j] = int(sessions[i][j])
new = []
constants = []
for i in range(len(sessions)):
    for j in range(len(sessions[i])-1):
        for l in range(j+1, len(sessions[i])):
            constants.append([sessions[i][j], sessions[i][l]])
            if [sessions[i][j], sessions[i][l]] not in new:
                new.append([sessions[i][j], sessions[i][l]])

count = 0

for i in range(len(new)):
    if constants.count(new[i]) == numSessions:
        count += 1

with open('gymnastics.out', 'w') as fout:
    #fout.write(str(new) + '\n')
    #fout.write(str(constants)+'\n')
    fout.write(str(count)+'\n')