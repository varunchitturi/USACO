x, y = input().split()
numCows = int(x)
budget = int(y)
orders = []
possibilities = []
for i in range(numCows):
    x, y = input().split()
    orders.append([int(x)+int(y), int(x), int(y)])

for i in range(numCows):
    orders[i][1] = int(orders[i][1]/2)
    orders[i][0] = orders[i][1] + orders[i][2]
    # print(orders)

    cost = 0
    count = 0
    a = sorted(orders)
    while True:
        cost += (a)[count][1] + (a)[count][2]
        count += 1
        if cost == budget:
            break
        elif cost > budget:
            count -= 1
            break
    possibilities.append(count)

    orders[i][1] = orders[i][1] * 2
    orders[i][0] = orders[i][1] + orders[i][2]
# print(possibilities)
try:
    print(max(possibilities))
except:
    print(0)
