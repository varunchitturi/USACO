def isLeapYear(year):
    if year % 4 == 0 and year % 100 != 0 and year % 400 != 0:
        return True
    if year % 4 == 0 and year % 100 == 0 and year % 400 == 0:
        return True
    if year % 4 == 0 and year % 100 == 0 and year % 400 != 0:
        return False
    else:
        return False
numYears = int(input())
startYear = 1900
#date = 1
dayNumber = 2
days = [31,28,31,30,31,30,31,31,30,31,30,31]
dayCount = [0,0,0,0,0,0,0]#saturday,sunday,monday,tuesday,wednesday,thursday,friday
for i in range (1900,1900+numYears):
    if isLeapYear(i) == True:
        days[1] = 29
    #for j in range (366):
        for k in range (12):
            for l in range (days[k]):
                if l == 12:
                    dayCount[dayNumber] += 1
                dayNumber = (dayNumber+1)%7
        days[1] = 28
    else:
    #for j in range (366):
        for k in range (12):
            for l in range (days[k]):
                if l == 12:
                    dayCount[dayNumber] += 1
                dayNumber = (dayNumber+1)%7

for i in range (7):
    print (dayCount[i],end=" ")
