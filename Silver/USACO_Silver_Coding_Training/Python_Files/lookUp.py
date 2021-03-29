numCows = int(input())
cowList = []
stack = []
for i in range(numCows):
    a = int(input())
    cowList.append(a)
    stack.append(i)

# print(stack)
j = 0
answers = [-1] * numCows
# print(answers)
for i in range(len(cowList)):

    while j > 0 and cowList[i] > cowList[stack[j - 1]]:
        j -= 1
        answers[stack[j]] = i

    stack[j] = i
    j += 1

for i in range(len(answers)):
    print(answers[i] + 1)
