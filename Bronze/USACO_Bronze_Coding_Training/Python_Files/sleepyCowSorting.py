import copy
def truncateList(list,index):
    truncatedList = []
    for i in range(index,len(list)):
        truncatedList.append(list[i])
    return truncatedList
x = int(input())

cowOrder = list(input().split())
for i in range (x):
    cowOrder[i] = int(cowOrder[i])

checkCowOrder = sorted(cowOrder)
flips = 0

cowOrder.reverse()
print (cowOrder)
for i in range (len(cowOrder)-2):
    if cowOrder[i] > cowOrder[i+1]:
        flips += 1
    else:
        break
print (x-flips-1)
