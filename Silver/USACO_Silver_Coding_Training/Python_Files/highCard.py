numElsieCards = int(input())
numCards = 2 * numElsieCards
elsieCards = []
bessieCards = []
for i in range(numElsieCards):
    elsieCards.append(int(input()))
elsieCards.sort(reverse=True)
current = 0
for i in range(numCards-1,-1,-1):
    if current >= numCards//2:
        break
    if i+1 == elsieCards[current]:
        current += 1
    else:
        bessieCards.append(i+1)

points = 0
bessieCards.sort(reverse=True)

#print(bessieCards)
#print(elsieCards)
while len(elsieCards) > 0:
    if bessieCards[0] > elsieCards[0]:
        del bessieCards[0]
        del elsieCards[0]
        points += 1
    else:
        del elsieCards[0]
print(points)

