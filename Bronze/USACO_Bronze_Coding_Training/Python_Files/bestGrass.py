def split(word):
    return list(word)



x,y = input().split()
length = int(x)
width = int(y)
array = []
for i in range (0,length):
    a = input()
    array.append(split(a))

count = 0
for i in range(0,len(array)):

    for j in range (0,len(array[0])):
        if array[i][j] == "#":
            count += 1
            array[i][j] = "."
            if j+1 == length and i+1 == width:
                break

            elif j+1 == width:
                array[i+1][j] = "."
                break
            elif i+1 == length:
                array[i][j+1] = "."

            else:
                array[i+1][j] = "."
                array[i][j+1] = "."
print(count)
