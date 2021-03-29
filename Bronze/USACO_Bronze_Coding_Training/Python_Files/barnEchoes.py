moo1 = list(input())
moo2 = list(input())
#for i in range len(moo1):
#    moo1[i] = ord(moo1[i])
#for i in range len(moo2):
#    moo2[i] = ord(moo2[i])
#prefix to suffix
check1 = []
i = 0
while True:
    check1.append(moo1[i])
    if "".join(check1) in "".join(moo2):
        i += 1
    else:
        break
#print (check1)
#print (moo1)
#print(moo2)
#check1 is how much it matches
check2 = []
i = 0
while True:
    check2.append(moo2[i])
    if "".join(check2) in "".join(moo1):
        i += 1
    else:
        break
print (max([len(check1),len(check2)])-1)
