import math


# f = open('inp.txt','r')
def inputmethod():
    return input()
    # return f.readline().strip()

def getCenterOfMass(pointsXY):
    xsum = sum(map(lambda p:p[0],pointsXY))
    ysum = sum(map(lambda p:p[1],pointsXY))
    n = len(pointsXY)

    return (xsum/n,ysum/n)

def getLen(v):
    return math.hypot(v[0],v[1])

def getTriArea(center,p1,p2):
    v1 = (p1[0]-center[0],p1[1]-center[1])
    v2 = (p2[0]-center[0],p2[1]-center[1])

    area2 = (v1[0]*v2[1]-v1[1]*v2[0])

    return area2


n = int(inputmethod())
pointsXY = []
for _ in range(n):
    XY = [*map(int,inputmethod().split(' '))]
    pointsXY.append(XY)

# print(f"{pointsXY=}")


centerX,centerY = getCenterOfMass(pointsXY)
center = (centerX,centerY)
# print(f"{center=}")

# pointsXY.sort(key=lambda p:math.atan2(p[1]-centerY,p[0]-centerX))

area2 = 0

for i in range(1,len(pointsXY)-1):
    p1 = pointsXY[i]
    p2 = pointsXY[(i+1)%n]

    areaDouble = getTriArea(pointsXY[0], p1, p2)
    # print(p1,p2,areaDouble)
    area2 += areaDouble

print(round(abs(area2)))