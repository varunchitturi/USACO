def secondsToTime(seconds):
    hoursRemainder = int(seconds%3600)
    hours = (seconds - hoursRemainder)/3600
    seconds -= hours*3600
    minutesRemainder=  int(seconds % 60)
    minutes = (seconds - minutesRemainder)/60
    seconds -= minutes*60
    return (str(int(hours)) + " " + str(int(minutes)) + " " + str(int(seconds)))

numberOfCows = int(input())
hours = []
minutes = []
seconds = []
for i in range (0,numberOfCows):
    x,y,z = input().split()
    hours.append(int(x))
    minutes.append(int(y))
    seconds.append(int(z))

totalTime = []
for i in range (numberOfCows):
    hoursToSeconds = hours[i]*3600
    minutesToSeconds = minutes[i]*60
    totalSeconds = minutesToSeconds+hoursToSeconds+seconds[i]
    totalTime.append(totalSeconds)
totalTime.sort()
for i in range (len(totalTime)):
    print(secondsToTime(totalTime[i]))
