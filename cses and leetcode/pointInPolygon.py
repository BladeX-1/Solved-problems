try:
    open("__localsystemflag__").close()
    f = open('inp.txt')
    fout = open('out.txt')
    env = 'local'
except FileNotFoundError:
    f = None
    fout = None
    env = 'server'

originalInput = input

from collections import namedtuple
import math
from fractions import Fraction
import time
# from numba import njit


def inputmethod():
    if f:
        return f.readline().strip()
    else:
        return originalInput()
input = inputmethod

def locationTest(polyPointsXY,x,y):
    p3 = Point(x,y)
    # rayX = p3.x + phi        phi>=0
    # rayY = p3.y
    # travels horizontally to the right, y is fix, x changes in positive
    boundaryHitCount = 0
    for i in range(len(polyPointsXY)):
        p1 = polyPointsXY[i]
        p2 = polyPointsXY[(i+1)%len(polyPointsXY)]

        # Ay+Bx+C = 0
        # (y-y1)*(x2-x1) = (y2-y1)*(x-x1)
        A = p2.x-p1.x
        B = p1.y-p2.y
        C = -p1.y*(p2.x-p1.x)+p1.x*(p2.y-p1.y)

        minX = min(p1.x,p2.x)
        minY = min(p1.y,p2.y)

        maxX = max(p1.x,p2.x)
        maxY = max(p1.y,p2.y)

        # deals properly with on-boundary cases
        if A*p3.y+B*p3.x+C==0\
            and minX<=p3.x<=maxX\
            and minY<=p3.y<=maxY:
            return "BOUNDARY"

        # surely NOT on boundary from now onwards

        # line = p1 + lambda*(p2-p1)

        # get lambda for p3
        if p2.y!=p1.y and maxX>p3.x and minY<=p3.y<=maxY: # NOT a horizontal line
            lambda_ = Fraction(p3.y-p1.y,p2.y-p1.y)

            # if not (0<=lambda_<=1):
            #     assert False
            #     # ray and segment DO NOT hit
            #     continue

            # skip the bottom point for boundary hit
            if lambda_==0 and p1.y<p2.y:
                continue
            elif lambda_==1 and p1.y>p2.y:
                continue

            xAtLambda = p1.x+lambda_*(p2.x-p1.x)
            rayX = xAtLambda

            # put ray == line
            phi = rayX - p3.x

            assert phi!=0

            if phi>0:
                boundaryHitCount += 1

    if boundaryHitCount%2==1:
        return "INSIDE"
    else:
        return "OUTSIDE"


vertices, lenPoints = [*map(int,input().split(' '))]

polygonXY = []
Point = namedtuple("Point",['x','y'])

for _ in range(vertices):
    x,y = map(int,input().split(' '))
    polygonXY.append(Point(x,y))
    

if env=="local":
    t = time.time()
answers = []
for i in range(lenPoints):

    x,y = map(int,input().split(' '))
    ans = locationTest(polygonXY,x,y)
    answers.append(ans)
    
print('\n'.join(answers))
if env=="local":
    print(time.time()-t)  # type: ignore