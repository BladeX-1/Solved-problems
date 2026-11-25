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
    n,m = [*map(int,inputmethod().split())]
    arrM = [*map(int,inputmethod().split())]
    arrM.sort()

    gapIntervals = []
    for i in range(m):
        intvl = (arrM[(i+1)%m]-arrM[i]-1+n)%n
        gapIntervals.append(intvl)

    gapIntervals.sort(reverse=True)

    daysPassed = 0
    saved = 0
    for i in range(len(gapIntervals)):
        intv = gapIntervals[i]-daysPassed*2

        if intv<=0:
            break
        if intv==1:
            saved+=1
            daysPassed+=1
        elif intv==2:
            saved+=1
            daysPassed+=1
        else:
            saved+=intv-1
            daysPassed+=2

    print(n-saved)