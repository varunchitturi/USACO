word1 = list(input())
word2 = list(input())
totalWord1 = 1
totalWord2 = 1
for i in range (len(word1)):
    totalWord1 = totalWord1 * ord(word1[i])
for i in range (len(word2)):
    totalWord2 = totalWord2 * ord(word1[i])
if totalWord1 % 47 == totalWord2 % 47:
    print("GO")
else:
    print("STAY")
