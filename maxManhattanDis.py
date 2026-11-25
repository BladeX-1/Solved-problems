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


n = int(inputmethod())
maxXPlusY = 0
minXPlusY = float('inf')
maxXMinusY = 0
minXMinusY = float('inf')
for _ in range(n):
    x,y = map(int,inputmethod().split(' '))

    maxXPlusY = max(maxXPlusY,x+y)
    minXPlusY = min(minXPlusY,x+y)

    maxXMinusY = max(maxXMinusY,x-y,y-x)
    minXMinusY = min(minXMinusY,x-y,y-x)

    a = maxXPlusY-minXPlusY
    b = maxXMinusY-minXMinusY

    print(max(a,b))
