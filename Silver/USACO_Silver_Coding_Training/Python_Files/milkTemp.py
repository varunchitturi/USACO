a, b, c, d = input().split()
numCows = int(a)
lowProduction = int(b)
bestProduction = int(c)
highProduction = int(d)
points = []
for i in range(numCows):
    x, y = input().split()
    points.append([int(x), -2])
    points.append([int(y), -1])
points.sort()
greatestProduction = -1
production = numCows * lowProduction
for i in range(len(points)):
    if points[i][1] == -2:
        production -= lowProduction
        production += bestProduction
    elif points[i][1] == -1:
        production -= bestProduction
        production += highProduction
    if production > greatestProduction:
        greatestProduction = production

print(greatestProduction)
