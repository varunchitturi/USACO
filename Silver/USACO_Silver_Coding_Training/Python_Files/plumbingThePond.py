x, y = input().split()
length = int(x)
width = int(y)
reading = []


def most_frequent(List):
    return max(set(List), key = List.count)


def maximum(list):
    return (max(map(max, reading)))


for i in range(length):
    reading.append(input().split())
for i in range(length):
    for j in range(width):
        reading[i][j] = int(reading[i][j])
addBorder = [0]*(width+2)
for i in range(length):
    reading[i].insert(0, 0)
    reading[i].append(0)
reading.insert(0, addBorder)
reading.append(addBorder)
verified = []
for i in range(1, length+1):
    for j in range(1, width+1):
        surround = [reading[i][j], reading[i-1][j], reading[i+1][j], reading[i][j-1], reading[i][j+1], reading[i-1][j-1], reading[i-1][j+1], reading[i+1][j-1], reading[i+1][j+1]]
        k = 0
        while k < len(surround):
            if surround[k] == 0:
                del surround[k]
            else:
                k += 1
        # print(surround)
        if surround.count(reading[i][j]) >= 2:
            verified.append(reading[i][j])
print(max(verified))
