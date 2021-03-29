numCommands = int(input())
stack = []
commands = []
for i in range(numCommands):
    x = input()
    commands.append(x)
count = 1
for i in range(len(commands)):
    if commands[i] == "ADD":
        stack.append(count)
        count += 1
    else:
        stack.pop()
print(len(stack))
for i in range(len(stack)):
    print(stack[i])
