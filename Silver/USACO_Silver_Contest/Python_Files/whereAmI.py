with open('whereami.in', 'r') as fin:
    length = int(fin.readline().strip())
    mailboxes = fin.readline().strip()

k = length
for i in range(1, len(mailboxes)+1):
    newList = []
    for j in range(len(mailboxes)-i+1):
        newList.append(mailboxes[j:j+i])
    x = list(set(newList))
    if len(x) == len(newList):
        k = i
        break
with open('whereami.out', 'w') as fout:
    # fout.write(str(new) + '\n')
    # fout.write(str(mailboxes[k:]))
    #fout.write(str(new))
    #fout.write(str(mailboxes[k:]))
    fout.write(str(k) + '\n')

