import sys
inputI = -1
inputArr = []
try:
    open("__localsystemflag__").close()
    f = open('inp.txt')
    env = 'local'
except FileNotFoundError:
    inputArr = sys.stdin.read().split('\n')
    inputI = 0
    f = None
    env = 'server'

def inputmethod():
    global inputI
    if f:
        return f.readline().strip()
    else:
        inputI+=1
        return inputArr[inputI-1]
        return input()



t = int(inputmethod())
for _ in range(t):
    delx,dely = [*map(int,inputmethod().split(' '))]
    ans = 0

    for i in range(2):
        xs = [*map(int,inputmethod().split(' '))]
        ans = max(ans,dely*(xs[-1]-xs[1]))

    for i in range(2):
        ys = [*map(int,inputmethod().split(' '))]
        ans = max(ans,delx*(ys[-1]-ys[1]))

    print(ans)