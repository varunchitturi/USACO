x,y = input().split()
roadSegments = int(x)
bessieSegments = int(y)
road = [] #distance, speed limit
bessie = [] #distance , speed
for i in range (roadSegments):
    x,y = input().split()
    distance1 = int(x)
    speedLimit = int(y)
    road.append([distance1 , speedLimit])
for i in range (bessieSegments):
    x,y = input().split()
    distance2 = int(x)
    speed = int(y)
    bessie.append([distance2,speed])
simRoad = []
simBessie = []
#print (road)
#print (bessie)
#print (roadSegments)
#print (bessieSegments)
for i in range (roadSegments):#initialize the road
    for j in range (road[i][0]):
        simRoad.append(road[i][1])
for i in range (bessieSegments):#initialize bessie
    for j in range (bessie[i][0]):
        simBessie.append(bessie[i][1])
max = 0
for i in range (100):
    if simBessie[i]-simRoad[i] > max:
        max = simBessie[i]-simRoad[i]
print (max)
#print (simRoad)
#print (simBessie)
