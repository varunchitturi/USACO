import math
x,y = input().split()
cowsRunning = int(x)
maxBVotes = 0
maxBVoteIndex = -1
advancingCows = int(y)
aVotes = []
bVotes = []
#advancingCowVotes = []
#package = []
x = 0
for i in range (cowsRunning):
    a,b = input().split()
    aVotes.append([int(a),i])
    bVotes.append(int(b))
#greatestVotes = []
aVotes.sort(reverse=True)

for i in range (advancingCows):

    x = int(aVotes[i][1])
    b = bVotes[x]
    if b>maxBVotes:
        maxBVotes = b
        maxBIndex = x

    #package = [b,x]
    #advancingCowVotes.append(package)
    #greatestVotes.append(advancingCowVotes[i][0])
# votes,index


#advancingCowVotes = sorted(advancingCowVotes, key=lambda x: x[0])

#final = advancingCowVotes[len(advancingCowVotes)-1][1]
print(maxBIndex + 1)
