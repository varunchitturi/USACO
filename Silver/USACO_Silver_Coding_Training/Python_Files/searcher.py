def findStart(a, lookFor):
    start = 0
    end = len(a)-1
    middle = len(a)//2
    while True:
        if lookFor < a[start]:
            return (start)
            break
        if lookFor > a[end]:
            return (end)
            break
        if a[start] < lookFor and a[middle] > lookFor and start + 1 == middle:
            return (middle)
            break
        if a[middle] < lookFor and a[end] > lookFor and middle + 1 == end:
            return (end)
            break
        if start == middle and a[start] < lookFor and a[end] > lookFor and start + 1 == end:
            return (end)
            break
        if middle == end and a[start] < lookFor and a[end] > lookFor and start + 1 == end:
            return (end)
            break
        if a[middle] == lookFor:
            return (middle)
            break
        if a[start] == lookFor:
            return(start)
            break
        if a[end] == lookFor:
            return (end)
            break
        if lookFor > a[start] and lookFor < a[middle]:
            end = middle
            middle = (start+middle)//2
        elif lookFor > a[middle] and lookFor < a[end]:
            start = middle
            middle = (end+middle)//2


def findEnd(a, lookFor):
    start = 0
    end = len(a)-1
    middle = len(a)//2
    while True:
        if lookFor < a[start]:
            return (start)
            break
        if lookFor > a[end]:
            return (end)
            break
        if a[start] < lookFor and a[middle] > lookFor and start + 1 == middle:
            return (start)
            break
        if a[middle] < lookFor and a[end] > lookFor and middle + 1 == end:
            return (middle)
            break
        if start == middle and a[start] < lookFor and a[end] > lookFor and start + 1 == end:
            return (start)
            break
        if middle == end and a[start] < lookFor and a[end] > lookFor and start + 1 == end:
            return (start)
            break
        if a[middle] == lookFor:
            return (middle)
            break
        if a[start] == lookFor:
            return(start)
            break
        if a[end] == lookFor:
            return (end)
            break
        if lookFor > a[start] and lookFor < a[middle]:
            end = middle
            middle = (start+middle)//2
        elif lookFor > a[middle] and lookFor < a[end]:
            start = middle
            middle = (end+middle)//2
