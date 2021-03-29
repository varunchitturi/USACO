numMeasurements = int(input())
measurements = []
for i in range(numMeasurements):
    measurements.append(int(input()))
greatest = 0
for i in range(numMeasurements):
    width = 1
    if greatest == numMeasurements:
        break
    if i == 0:
        for j in range(i, numMeasurements-1):
            if measurements[j + 1] <= measurements[j]:
                width += 1
            else:
                break
    elif i == numMeasurements - 1:
        for j in range(i, 0, -1):
            if measurements[j - 1] <= measurements[j]:
                width += 1
            else:
                break
    else:

        for j in range(i, numMeasurements-1):
            if measurements[j+1] <= measurements[j]:
                width += 1
            else:
                break
        for j in range(i,0,-1):
            if measurements[j-1] <= measurements[j]:
                width += 1
            else:
                break
    if width > greatest:
        greatest = width



print(greatest)