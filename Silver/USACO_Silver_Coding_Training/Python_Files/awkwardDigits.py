binary = input()
trinary = input()
possibleBinary = []
possibleTrinary = []
def intersection(lst1, lst2):
    return list(set(lst1) & set(lst2))
def bintodec(bin):
    dec = 0
    for i in range(len(bin)):
        dec += 2**(len(bin)-1-i)*int(bin[i])
    return dec
def trintodec(trin):
    dec = 0
    for i in range(len(trin)):
        dec += 3**(len(trin)-1-i)*int(trin[i])
    return dec
for i in range(len(binary)):
    a = list(binary)
    if a[i] == '0':
        a[i] = '1'
        possibleBinary.append(bintodec("".join(a)))
    else:
        a[i] = '0'
        possibleBinary.append(bintodec("".join(a)))



for i in range(len(trinary)):
    a = list(trinary)
    if a[i] == '0':
        a[i] = '1'
        possibleTrinary.append(trintodec("".join(a)))
        a[i] = '2'
        possibleTrinary.append((trintodec("".join(a))))
    elif a[i] == '1':
        a[i] = '0'
        possibleTrinary.append((trintodec("".join(a))))
        a[i] = '2'
        possibleTrinary.append((trintodec("".join(a))))
    else:
        a[i] = '1'
        possibleTrinary.append((trintodec("".join(a))))
        a[i] = '0'
        possibleTrinary.append((trintodec("".join(a))))
print(intersection(possibleTrinary,possibleBinary)[0])