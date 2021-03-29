numRegisters  = int(input())
line = []
registers = []
for i in range(numRegisters):
    registers.append([])
while(True):
    try:
        x, y = input().split()
        type = x
        id = int(y)
        if type == "C":
            line.append(id)
        else:
            registers[id-1].append(line[0])
            del line[0]
    except:
        break
for i in range(numRegisters):
    print(len(registers[i]), end = " ")
    for j in range(len(registers[i])):
        print(registers[i][j], end = " ")
    print()