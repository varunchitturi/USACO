def removeDuplicates(x):
  return list(dict.fromkeys(x))
def split(word):
    return [char for char in word]
numEntries = int(input())
entryDay = []
name = []
changeInProduction = []
initial = [7,7,7]
championsBefore = ["Bessie","Elsie","Mildred"]
championsAfter = []
changes = 0
otherName = ["Bessie","Elsie","Mildred"]
for i in range (numEntries):
    x,y,z = input().split()
    entryDay.append([int(x),i])
    name.append(y)
    z = split(z)
    if z[0] == "+":
        changeInProduction.append(int(z[1]))
    else:
        z = "".join(z)
        changeInProduction.append(int(z))

entryDay.sort()

#print(len(entryDay))
#print(entryDay)
#print(name)
#print(changeInProduction)
for i in range (0,len(entryDay)):


    if name[entryDay[i][1]] == "Bessie":
        initial[0]+=changeInProduction[entryDay[i][1]]
        #print(initial)
    elif name[entryDay[i][1]] == "Elsie":
        initial[1]+=changeInProduction[entryDay[i][1]]
        #print(initial)
    elif name[entryDay[i][1]] == "Mildred":
        initial[2]+=changeInProduction[entryDay[i][1]]
        #print(initial)
    maximum = max(initial)

    for i in range (len(initial)):
        if initial[i] == maximum:
            championsAfter.append(otherName[i])
            championsAfter=removeDuplicates(championsAfter)
            #print(championsAfter)
    if championsBefore != championsAfter:
        changes+=1
        championsBefore=championsAfter
        championsAfter=[]
    championsAfter = []
print(changes)
