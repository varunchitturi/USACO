import sys
numberOfDays = int(input())
logs = input().split()

for i in range (len(logs)):
    logs[i] = int(logs[i])

for i in range (len(logs)-1):
    if logs[i] == logs[i+1] and logs[i] != 0 and logs[i] != -1:
        print(-1)

        sys.exit()
#for i in range (len(logs)-1):
#    if logs[i] != 0 and logs[i] != -1 and logs[i+1] < logs[i]:
#        logs[i] = -1
logs[0] = 0

for i in range (len(logs)):
    if logs[i] >=1:
        logs[i-logs[i]] = 0
print (logs.count(0),end=" ")
for i in range(len(logs)-1,0,-1):
    if logs[i] > 1:
        logs[i-1] = logs[i] -1

total = logs.count(0) + logs.count(-1)
print (total)
