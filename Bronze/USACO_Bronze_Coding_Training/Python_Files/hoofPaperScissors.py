#inputs
numOfPlays = int(input())
cow1 = []
cow2 = []
for i in range (0,numOfPlays):
    x,y = input().split()
    cow1.append(int(x))
    cow2.append(int(y))
wins = []
#1 is hoof
#2 is paper
#3 is scissors
sum1 = 0
sum2 = 0
sum3 = 0
sum4 = 0
sum5 = 0
sum6 = 0
for i in range (0,numOfPlays):
    if cow1[i] == 1 and cow2[i] == 1:
        sum1 +=0
    if cow1[i] == 1 and cow2[i] == 2:
        sum1 +=0
    if cow1[i] == 1 and cow2[i] == 3:
        sum1 +=1
    if cow1[i] == 2 and cow2[i] == 1:
        sum1 +=1
    if cow1[i] == 2 and cow2[i] == 2:
        sum1 +=0
    if cow1[i] == 2 and cow2[i] == 3:
        sum1 +=0
    if cow1[i] == 3 and cow2[i] == 1:
        sum1 +=0
    if cow1[i] == 3 and cow2[i] == 2:
        sum1 +=1
    if cow1[i] == 3 and cow2[i] == 3:
        sum1 +=0
#1 is hoof
#2 is scissors
#3 is paper
for i in range (0,numOfPlays):
    if cow1[i] == 1 and cow2[i] == 1:
        sum2 +=0
    if cow1[i] == 1 and cow2[i] == 2:
        sum2 +=1
    if cow1[i] == 1 and cow2[i] == 3:
        sum2 +=0
    if cow1[i] == 2 and cow2[i] == 1:
        sum2 +=0
    if cow1[i] == 2 and cow2[i] == 2:
        sum2 +=0
    if cow1[i] == 2 and cow2[i] == 3:
        sum2 +=1
    if cow1[i] == 3 and cow2[i] == 1:
        sum2 +=1
    if cow1[i] == 3 and cow2[i] == 2:
        sum2 +=0
    if cow1[i] == 3 and cow2[i] == 3:
        sum2 +=0


#1 is paper
#2 is hoof
#3 is scissors
for i in range (0,numOfPlays):
    if cow1[i] == 1 and cow2[i] == 1:
        sum3 +=0
    if cow1[i] == 1 and cow2[i] == 2:
        sum3 +=1
    if cow1[i] == 1 and cow2[i] == 3:
        sum3 +=0
    if cow1[i] == 2 and cow2[i] == 1:
        sum3 +=0
    if cow1[i] == 2 and cow2[i] == 2:
        sum3 +=0
    if cow1[i] == 2 and cow2[i] == 3:
        sum3 +=1
    if cow1[i] == 3 and cow2[i] == 1:
        sum3 +=1
    if cow1[i] == 3 and cow2[i] == 2:
        sum3 +=0
    if cow1[i] == 3 and cow2[i] == 3:
        sum3 +=0


#1 is paper
#2 is scissors
#3 is hoof
for i in range (0,numOfPlays):
    if cow1[i] == 1 and cow2[i] == 1:
        sum4 +=0
    if cow1[i] == 1 and cow2[i] == 2:
        sum4 +=0
    if cow1[i] == 1 and cow2[i] == 3:
        sum4 +=1
    if cow1[i] == 2 and cow2[i] == 1:
        sum4 +=1
    if cow1[i] == 2 and cow2[i] == 2:
        sum4 +=0
    if cow1[i] == 2 and cow2[i] == 3:
        sum4 +=0
    if cow1[i] == 3 and cow2[i] == 1:
        sum4 +=0
    if cow1[i] == 3 and cow2[i] == 2:
        sum4 +=1
    if cow1[i] == 3 and cow2[i] == 3:
        sum4 +=0


#1 is scissors
#2 is hoof
#3 is paper
for i in range (0,numOfPlays):
    if cow1[i] == 1 and cow2[i] == 1:
        sum5 +=0
    if cow1[i] == 1 and cow2[i] == 2:
        sum5 +=0
    if cow1[i] == 1 and cow2[i] == 3:
        sum5 +=1
    if cow1[i] == 2 and cow2[i] == 1:
        sum5 +=1
    if cow1[i] == 2 and cow2[i] == 2:
        sum5 +=0
    if cow1[i] == 2 and cow2[i] == 3:
        sum5 +=0
    if cow1[i] == 3 and cow2[i] == 1:
        sum5 +=0
    if cow1[i] == 3 and cow2[i] == 2:
        sum5 +=1
    if cow1[i] == 3 and cow2[i] == 3:
        sum5 +=0


#1 is scissors
#2 is paper
#3 is hoof
for i in range (0,numOfPlays):
    if cow1[i] == 1 and cow2[i] == 1:
        sum6 +=0
    if cow1[i] == 1 and cow2[i] == 2:
        sum6 +=1
    if cow1[i] == 1 and cow2[i] == 3:
        sum6 +=0
    if cow1[i] == 2 and cow2[i] == 1:
        sum6 +=0
    if cow1[i] == 2 and cow2[i] == 2:
        sum6 +=0
    if cow1[i] == 2 and cow2[i] == 3:
        sum6 +=1
    if cow1[i] == 3 and cow2[i] == 1:
        sum6 +=1
    if cow1[i] == 3 and cow2[i] == 2:
        sum6 +=0
    if cow1[i] == 3 and cow2[i] == 3:
        sum6 +=0
wins = [sum1,sum2,sum3,sum4,sum5,sum6]
print(max(wins))
