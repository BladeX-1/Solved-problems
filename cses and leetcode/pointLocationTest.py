try:
    open("__localsystemflag__x").close()
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

import math


# (y-y1)*(x2-x1) = (y2-y1)*(x-x1)
# A*y + B*x + C = 0

t = int(inputmethod())
for _ in range(t):
    x1,y1, x2,y2, x3,y3 = [*map(int,inputmethod().split(' '))]

    A = x2-x1
    B = -(y2-y1)
    C = -y1*(x2-x1)-(-x1*(y2-y1))

    # (inf,0) will be of sign 'B'
    # (0,inf) will be of sign 'A'
    signLocation = A*y3+B*x3+C




    if signLocation==0:
        print("TOUCH")

    # p1 is below p2 so same sign as B means right, else switch signs
    elif y1!=y2 and signLocation*B*(y2-y1)>0\
        or x1!=x2 and signLocation*A*(x1-x2)>0: # same sign as 'B'
            print("RIGHT")
    else:
        print("LEFT")