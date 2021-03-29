def double(array):
    for a in range(len(array)):
        array[a] = [array[a][0],array[a][0]]
numCows = int(input())
ID = []
shuffle = []
#index = []
shuffle = input().split()
shuffle = [ int(x) for x in shuffle ]
ID = input().split()
ID = [ int(x) for x in ID ]
for i in range (len(ID)):
    ID[i] = [ID[i],ID[i]]
#for i in range(numCows):
#    index.append(i)
#print (ID)
#print(shuffle)
for i in range (3):
    for j in range (numCows):
        ID[j][0] = ID[shuffle[j]-1][1]
        #print(shuffle[j]-1)
        #print (ID)

    double(ID)
    #print (ID)
for i in range (len(ID)):
    print(ID[i][0])
