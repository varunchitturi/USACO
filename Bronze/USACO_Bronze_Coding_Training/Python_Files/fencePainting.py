a,b = input().split()
c,d = input().split()
list = [int(a),int(b),int(c),int(d)]

if list[2] > list[1]:
    print ((list[1]-list[0])+(list[3]-list[2]))
elif list[0] > list[3]:
    print ((list[1]-list[0])+(list[3]-list[2]))







else:
    print(max(list)-min(list))
