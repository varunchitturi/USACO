a,b = input().split()
phrase = list(a)
size = int(b)


operations = 0
leng = len(phrase)
while(leng < size):
    leng *= 2
    operations += 1
position = size

#print(position)
#print(operations)
for i in range(operations):
    if(position == leng//2 + 1):
        position -= 1
    elif position > leng//2:
        position = position - leng//2 - 1
    leng = leng//2
    #print(position)
    #print(leng)
print (phrase[position - 1])

#C   O   W   W   C   O   O   C   O   W   W   C
#1   2   3   4   5   6   7   8
