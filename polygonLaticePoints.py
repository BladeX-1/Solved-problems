try:
    open("__localsystemflag__").close()
    f = open('inp.txt')
    env = 'local'
except FileNotFoundError:
    f = None
    env = 'server'

def inputmethod():
    if f:
        return f.readline().strip()
    else:
        return input()


n = int(input())
poly = []

from collections import namedtuple
import math
from fractions import Fraction
Point = namedtuple("Point",["x","y"])

for _ in range(n):
    pointxy = Point(*map(int,input().split()))
    poly.append(pointxy)


for i in range(len(poly)):
    p1 = poly[i]
    p2 = poly[(i+1)%len(poly)]

    if p1.y == p2.y:
        # skip horizontal lines
        continue

    isHorizontal = False
    if p2.y>p1.y:
        rayIsUp = True
    elif p2.y<p1.y:
        rayIsUp = False
    else:
        isHorizontal = True

    # we'll throw rays from p1 to p2
    m = Fraction(p2.y-p1.y,p2.x-p1.x)
    c = m*(-p1.x)+p1.y
    # y = mx+c

    # total #row = p2.y-p1.y+1
    # first change dx = 1
    # first change dy = m
    