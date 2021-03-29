lawnMower = input().split()
for i in range (len(lawnMower)):
    lawnMower[i]= int(lawnMower[i])
cowFeed = input().split()
for i in range (len(cowFeed)):
    cowFeed[i]= int(cowFeed[i])
Lx1 =lawnMower[0]
Lx2 = lawnMower[2]
Ly1 = lawnMower[1]
Ly2 = lawnMower[3]
Cx1 = cowFeed[0]
Cx2 = cowFeed[2]
Cy1 = cowFeed[1]
Cy2 = cowFeed[3]

area = 0
if (Lx1 >= Cx1 and Lx1 <= Cx2 and Ly2 <= Cy2 and Ly2 >= Cy1 and Lx2 <= Cx2 and Lx2 >=  Cx1 and Ly1 >= Cy1 and Ly1 < Cy2):
    area = 0
#4
elif (Lx1 < Cx1 and Lx2 > Cx2) or (Ly1 < Cy1 and Ly2 > Cy2) or (Lx2 < Cx1) or (Lx1> Cx2) or (Ly2<Cy1) or (Ly1 > Cy2 ):
    area = abs((Lx2 - Lx1))*abs((Ly2 - Ly1))

#3 are out proofread this done
elif (Lx1 < Cx1 and Ly2 > Cy2 and Ly1<Cy2 and Ly1>Cy1) or (Lx1 < Cx1 and Ly1 < Cy1 and Ly2 > Cy1 and Ly2< Cy2) or (Lx2 > Cx2 and Ly2 > Cy2 and Ly1<Cy2 and Ly1 > Cy1) or (Lx2 > Cx2 and Ly2 < Cy2 and Ly2 > Cy1 and Ly1 < Cy1):
    area = abs((Lx2 - Lx1))*abs((Ly2 - Ly1))
#2 are out maybe put this after 0 are out
#elif (Lx1 < Cx1 and Lx2 > Cx1 and Lx2 < Cx2) or (Ly2 > Cy2 and Ly1 < Cy2 and Ly1 > Cy1) or (Lx2 > Cx2 and Lx1 > Cx1 and Lx1 < Cx2) or (Ly1<Cy1 and Ly2<Cy2 and Ly2 > Cy1)

elif (Lx1 < Cx1 and Lx2 > Cx1 and Lx2 < Cx2):
    area = (Cx1-Lx1)*(Ly2-Ly1)
elif (Ly2 > Cy2 and Ly1 < Cy2 and Ly1 > Cy1):
    area = (Lx2-Lx1)*(Ly2-Cy2)
elif (Lx2 > Cx2 and Lx1 > Cx1 and Lx1 < Cx2):
    area = (Ly2-Ly1)*(Lx2-Cx2)
elif (Ly1<Cy1 and Ly2<Cy2 and Ly2 > Cy1):
    area = (Lx2-Lx1)*(Cy1-Ly1)

#0 are out do greater or equal done

print (area)
