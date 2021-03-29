numTimes = int(input())
times = []
longestMilkTimes = []
longestStopTimes = []
for i in range(numTimes):
    x, y = input().split()
    start = int(x)
    stop = int(y)
    times.append([start, "start"])
    times.append([stop, "stop"])
status = 0
begin = times[0][0]
end = 0
times.sort()
for i in range(len(times)):
    if times[i][1] == "start" and status == 0:
        begin = times[i][0]
        status += 1
    elif times[i][1] == "start" and status != 0:
        status += 1
    if times[i][1] == "stop":
        status -= 1
        end = times[i][0]
    if status == 0:
        longestMilkTimes.append(end-begin)
    if status == 0 and i != len(times)-1 and times[i][1] == "stop":
        longestStopTimes.append(times[i+1][0]-times[i][0])
    # print(status)
if len(longestMilkTimes) == 0:
    print(0)
else:
    print(max(longestMilkTimes), end=" ")
if len(longestStopTimes) == 0:
    print(0)
else:
    print(max(longestStopTimes))
# print(times)
