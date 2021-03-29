# use reverse indexing!!!
x, y = input().split()
numStacks = int(x)
stacks = [0]*(numStacks+2)
numInstructions = int(y)
rangeArray = []
diffArray = []
# print(stacks)
for i in range(numInstructions):
    a, b = input().split()
    stacks[int(a)] += 1
    stacks[int(b)+1] -= 1
# print(stacks)
count = 0
for i in range(len(stacks)):
    count += stacks[i]
    stacks[i] = count

stacks.sort()
print (stacks[(len(stacks)//2)+1])
