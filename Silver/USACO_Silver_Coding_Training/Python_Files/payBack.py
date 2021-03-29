numTransaction = int(input())
transactions = []
completedCount = 0
for i in range(numTransaction):
    transactions.append(int(input()))
i = 0
money = 0
toPay = []
totalDistanceMoved = 0
def getsum(array):
    sum = 0
    for i in range(len(array)):
        sum += array[i][1]
    return sum
def checkPay(currentPosition, currentMoney, distanceMoved, completed):
    position = currentPosition
    for i in range(len(toPay)):
        if toPay[i][1] + currentMoney >= 0:
            distanceMoved += (abs(toPay[i][0]-position))
            position = toPay[i][0]
            currentMoney += toPay[i][1]
            toPay[i] = 'none'
            completed += 1
    while 'none' in toPay:
        toPay.remove('none')
    if position != currentPosition:
        distanceMoved += abs(position-currentPosition)
    return [currentMoney, distanceMoved, completed]


totalDistanceMoved += 1
while completedCount <= numTransaction:
    if i >= numTransaction:
        break
    if transactions[i] > 0:
        money += transactions[i]
        completedCount += 1
        if len(toPay) != 0 and -1*getsum(toPay) <= money:
            new =  checkPay(i, money, totalDistanceMoved, completedCount)
            money = new[0]
            totalDistanceMoved = new[1]
            completedCount = new[2]
    elif transactions[i] < 0:
        if money + transactions[i] >= 0:
            money += transactions[i]
            completedCount += 1
        else:
            toPay.append([i, transactions[i]])
    i += 1
    if i >= numTransaction:
        break
    totalDistanceMoved += 1
print(totalDistanceMoved)


