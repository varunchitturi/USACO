numPiles = int(input())
piles = []
sum = 0
for i in range(numPiles):
    x = int(input())
    piles.append(x)
    sum += x
averageHeight = sum/numPiles
piecesToMove = 0
for i in range(numPiles):
    if piles[i] < averageHeight:
        piecesToMove += averageHeight-piles[i]
print(int(piecesToMove))