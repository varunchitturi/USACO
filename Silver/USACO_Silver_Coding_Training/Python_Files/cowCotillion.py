numVariations = int(input())
variations = []
def findPair(a, length, phrase):
    for i in range(a, length):
        if phrase[i] == "<":
            phrase = list(phrase)
            phrase[a] = "@"
            phrase[i] = "@"
            "".join(phrase)
            return [True, phrase]
    return [-1, phrase]
for i in range(numVariations):
    x,y = input().split()
    variations.append([int(x), y])
# print(variations)
for i in range(numVariations):
    if variations[i][0] % 2 != 0:
        print("illegal")

    else:
        check = True
        phrase = variations[i][1]
        length = variations[i][0]
        for j in range(length):
            if phrase[j] == ">":
                place = findPair(j,length,phrase)
                if place[0] == -1:
                    print ("illegal")
                    check = False
                    break
                phrase = place[1]
        if check is True:
            if ("<" not in phrase and ">" not in phrase):
                print ("legal")
            else:
                print("illegal")
