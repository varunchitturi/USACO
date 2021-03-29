
def addTime(hours1,minutes1,hours2,minutes2):
    minutes = minutes1 + minutes2
    hours = hours1 + hours2
    if minutes / 60 >= 1:
        remainder = minutes % 60
        hours += (minutes-remainder)/60
        minutes -= (minutes-remainder)
        return [int(hours),minutes]
    else:
        return[int(hours),int(minutes)]
def timeDifference(hours1,minutes1,hours2,minutes2):
    minutes1 += (hours1*60)
    minutes2 += (hours2*60)
    minuteDifference = minutes1 - minutes2
    remainder = minuteDifference % 60
    hours = int((minuteDifference - remainder) / 60)
    minutes = remainder
    return [hours,minutes]



#inputs
x,y = input().split()
numberOfCows = int(x)
totalEntries = int(y)
cowNumber = []
startStop = []
hours = []
minutes = []
for i in range(0,totalEntries):
    a,b,c,d = input().split()
    cowNumber.append(int(a))
    startStop.append(b)
    hours.append(int(c))
    minutes.append(int(d))
maxCowNumbers = []
for i in range (0,max(cowNumber)):
    maxCowNumbers.append(i+1)


#program



for i in range (0,max(cowNumber)):
    sum = [0,0]
    for j in range(0,totalEntries):
        if cowNumber[j] == (i+1) and startStop[j] == "START":
            minutes1 = minutes[j]
            hours1 = hours[j]
            startStop[j] = "null"
            for k in range (j,totalEntries):
                if startStop[k] == "STOP" and cowNumber[k]==(i+1):
                    minutes2 = minutes[k]
                    hours2 = hours[k]
                    startStop[k] = "null"
                    difference = timeDifference(hours2,minutes2,hours1,minutes1)
                    k = 0
                    break
            sum = addTime(sum[0],sum[1],difference[0],difference[1])
    #print eachsum
    print (sum[0],end=" ")
    print (sum[1])
