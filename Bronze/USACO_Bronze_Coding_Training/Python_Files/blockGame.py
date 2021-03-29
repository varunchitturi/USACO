def stringToNum(string):
    if string == "a":
        return 1
    if string == "b":
        return 2
    if string == "c":
        return 3
    if string == "d":
        return 4
    if string == "e":
        return 5
    if string == "f":
        return 6
    if string == "g":
        return 7
    if string == "h":
        return 8
    if string == "i":
        return 9
    if string == "j":
        return 10
    if string == "k":
        return 11
    if string == "l":
        return 12
    if string == "m":
        return 13
    if string == "n":
        return 14
    if string == "o":
        return 15
    if string == "p":
        return 16
    if string == "q":
        return 17
    if string == "r":
        return 18
    if string == "s":
        return 19
    if string == "t":
        return 20
    if string == "u":
        return 21
    if string == "v":
        return 22
    if string == "w":
        return 23
    if string == "x":
        return 24
    if string == "y":
        return 25
    if string == "z":
        return 26
def numToString(num):
    if num == 1:
        return "a"
    if num == 2:
        return "b"
    if num == 3:
        return "c"
    if num == 4:
        return "d"
    if num == 5:
        return "e"
    if num == 6:
        return "f"
    if num == 7 :
        return "g"
    if num == 8:
        return "h"
    if num == 9:
        return "i"
    if num == 10:
        return "j"
    if num == 11:
        return "k"
    if num == 12:
        return "l"
    if num == 13:
        return "m"
    if num == 14:
        return "n"
    if num == 15:
        return "o"
    if num == 16:
        return "p"
    if num == 17:
        return "q"
    if num == 18:
        return "r"
    if num == 19:
        return "s"
    if num == 20:
        return "t"
    if num == 21:
        return "u"
    if num == 22:
        return "v"
    if num == 23:
        return "w"
    if num == 24:
        return "x"
    if num == 25:
        return "y"
    if num == 26:
        return "z"

boards = int(input())
list = []
for i in range (boards):
    x = input().split()
    list.append(x)
toPrint = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
for i in range (1,27):
    for j in range (boards):
        toPrint[i-1] +=  max([list[j][0].count(numToString(i)),list[j][1].count(numToString(i))])
for i in range (len(toPrint)):
    print(toPrint[i])
