import sys
inputI = -1
inputArr = []
spliter = "\n"
try:
    open("__localsystemflag__").close()
    f = open('inp.txt')
    env = 'local'
except FileNotFoundError:
    rawInput = sys.stdin.read()
    inputArr = rawInput.splitlines()
    
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
    n,k = [*map(int,inputmethod().split())]
    items = inputmethod().strip()

    bag1left = k
    bag2left = k

    newStart = 0
    bag1HasGlass = False
    bag2HasGlass = False
    possible = True
    for i in range(n):
        c = items[i]
        if c=='I':
            if not bag2HasGlass:
                # put I in bag2 freely, which is identical to skiping it
                continue
            elif bag2left-2>=0:
                bag2left-=2
            elif bag1left-2>=0:
                bag1left-=2
            else:
                possible = False
                break
        if c=='G':
            if not bag1HasGlass:
                # put first glass in bag1
                bag1HasGlass = True
            elif bag1left-1>=0:
                bag1left-=1
            elif not bag2HasGlass:
                # put the first glass in bag 2
                bag2HasGlass = True
            elif bag2left-1>=0:
                bag2left-=1
            else:
                possible = False
                break

    if possible:
        print("YES")
    else:
        print("NO")