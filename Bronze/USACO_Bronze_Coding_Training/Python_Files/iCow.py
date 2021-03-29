import math

# returns at which index point is the greatest number
def maximum(numbers):
	maxNum = max(numbers)
	for i in range(0,len(numbers)):
		if numbers[i] == maxNum:
			return (i)


# inputs
x,y = input().split()
numberOfSongs = int(x)
numberOfPlays = int(y)
ratings = []
for i in range (0,numberOfSongs):
	a = input()
	ratings.append(int(a))

# math
print(maximum(ratings)+1)
for i in range (0,numberOfPlays-1):
  greatestRating = max(ratings)
  maximumRatingPlacement = int(maximum(ratings))

  remainder = int(greatestRating)%int((len(ratings)-1))
  initialAdd = ((int(greatestRating))-int(remainder))/(len(ratings)-1)


  ratings.remove(max(ratings))

  for i in range (0,len(ratings)):
  	ratings[i] += initialAdd

  if remainder > 0:
    runTime = remainder
    for i in range (0,runTime):
      ratings[i] += 1
      remainder -= 1
  ratings.insert(maximumRatingPlacement,0)
  print (maximum(ratings)+1)
