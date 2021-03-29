x,y = input().split()
numHayBales = int(x)
farmersPurchasing = int(y)
prices = []
for i in range (farmersPurchasing):
    prices.append(int(input()))
prices.sort()
totals = []
for i in range (len(prices)):
    if farmersPurchasing-i > numHayBales:
        totals.append([(prices[i]*(numHayBales)),prices[i]])
    else:
        totals.append([(prices[i]*(farmersPurchasing-i)),prices[i]])
totals.sort(reverse=True)

print (totals[0][1],end=" ")
print (totals[0][0],end=" ")
