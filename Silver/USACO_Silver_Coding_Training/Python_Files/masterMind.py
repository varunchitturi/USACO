numGuesses = int(input())
gueses = []
for i in range(numGuesses):
    a,b,c = input().split()
    guess = a
    numRightPlace = int(b)
    numRightNumber = int(c)
    gueses.append([guess, numRightPlace, numRightNumber])
answer = "NONE"

def checkPlace(num, guess, numPlace, numRight):
    num = list(num)
    guess = list(guess)
    corrects = []
    count = 0
    for i in range(4):
        if num[i] == guess[i]:
            count += 1
            corrects.append(num[i]) #5
    if count != numPlace:
        return False
    else:
        count = 0
        for i in range(len(corrects)):
            for j in range(len(num)):
                if corrects[i] == num[j]:
                    del num[j]
                    break
            for j in range(len(guess)):
                if corrects[i] == guess[j]:
                    del guess[j]
                    break
                    # 123 137
        num = sorted(num)
        guess = sorted(guess)
        for i in range(len(num)):
            if guess[i] in num:
                count += 1
        if count != numRight:
            return False
        return True







def check(num):

    for i in range(len(gueses)):
        if(checkPlace(num, gueses[i][0], gueses[i][1], gueses[i][2]) is False):
            return False
    return True
h = False
for i in range(1000,10000):
    if(check(str(i))):
        print(i)
        h = True

        break
if h is False:
    print("NONE")
