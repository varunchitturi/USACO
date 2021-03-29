import sys
def removeDuplicates(x):
  return list(dict.fromkeys(x))
numEntries = int(input())
cows = [[0,"Bessie"],[0,"Elsie"],[0,"Daisy"],[0,"Gertie"],[0,"Annabelle"],[0,"Maggie"],[0,"Henrietta"]]
cowEntries = []
milkProduction = []
rankings = []
for i in range (numEntries):
    x,y = input().split()
    cowEntries.append(x)
    milkProduction.append(int(y))
    if cowEntries[i] == "Bessie":
        cows[0][0] += milkProduction[i]
    if cowEntries[i] == "Elsie":
        cows[1][0] += milkProduction[i]
    if cowEntries[i] == "Daisy":
        cows[2][0] += milkProduction[i]
    if cowEntries[i] == "Gertie":
        cows[3][0] += milkProduction[i]
    if cowEntries[i] == "Annabelle":
        cows[4][0] += milkProduction[i]
    if cowEntries[i] == "Maggie":
        cows[5][0] += milkProduction[i]
    if cowEntries[i] == "Henrietta":
        cows[6][0] += milkProduction[i]
cows.sort()

for i in range (len(cows)):
    rankings.append(cows[i][0])
rankings = removeDuplicates(rankings)
if len(rankings) == 1:
    print("Tie")
    sys.exit()
rankings.sort()
secondWorst = rankings[1]

answer = []
for i in range (len(cows)):
    if cows[i][0] == secondWorst:
        answer.append(cows[i][1])
if len(answer) == 1:
    print (" ".join(answer))
elif len(answer) == numEntries:
    print ("Tie")

else:
    removeDuplicates(answer)
    print (" ".join(answer))
