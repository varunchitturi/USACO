greatestNum = int(input())
x, y, z = input().split()
farmer = [int(x), int(y), int(z)]
x, y, z = input().split()
master = [int(x), int(y), int(z)]
lock = []
for i in range(greatestNum):
    lock.append(i+1)
possiblities = []
for i in range(-2, 3):
    for j in range(-2, 3):
        for k in range(-2, 3):
            possiblities.append([(lock[(lock.index(farmer[0])-i) % greatestNum]), (lock[(lock.index(farmer[1])-j) % greatestNum]), (lock[(lock.index(farmer[2])-k) % greatestNum])])
for i in range(-2, 3):
    for j in range(-2, 3):
        for k in range(-2, 3):
            possiblities.append([(lock[(lock.index(master[0])-i) % greatestNum]), (lock[(lock.index(master[1])-j) % greatestNum]), (lock[(lock.index(master[2])-k) % greatestNum])])


def unique(array):
    result = []
    for x in array:
        if x not in result:
            result.append(x)
    return result
print(len(unique(possiblities)))
