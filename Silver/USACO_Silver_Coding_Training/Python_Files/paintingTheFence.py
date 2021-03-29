numCommands = int(input())
commands = []
for i in range(numCommands):
    x,y = input().split()
    commands.append([int(x),y])
currentPosition = 0
doublePainted = 0
intervals = []
for i in range(numCommands):
    if commands[i][1] == "L":
        intervals.append([currentPosition - commands[i][0], currentPosition])
        currentPosition -= commands[i][0]
    elif commands[i][1] == "R":
        intervals.append([currentPosition, currentPosition + commands[i][0]])
        currentPosition += commands[i][0]
events = []
for i in range(len(intervals)):
    events.append([intervals[i][0], 1])
    events.append([intervals[i][1], -1])
events.sort()


def findStop(position):
    status1 = 2
    for i in range(position + 1, len(events)):

        status1 += events[i][1]
        if status1 == 1:
            return i
status = 0
check = True
i = 0
while i < len(events):
    status += events[i][1]
    position = events[i][0]
    if status == 2:
        a = findStop(i)
        doublePainted += abs(position - events[a][0])
        i = a
    else:
        i += 1
print(doublePainted)