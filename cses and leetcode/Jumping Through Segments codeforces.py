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

import itertools

def tryFill(maxJump,segments):
    newRange = [0,0]
    for i in range(len(segments)):
        l,r = segments[i]
        newRange = [max(l,newRange[0]-maxJump),min(r,newRange[1]+maxJump)]
        if newRange[1]<newRange[0]:
            return False

    return True

t = int(inputmethod())
for _ in range(t):
    n = int(inputmethod())
    segments = []
    for _n in range(n):
        segment = [*map(int,inputmethod().split())]
        segments.append(segment)

    low = max(segments[0][0],-segments[0][1],0)
    high = max(segments[0][1],-segments[0][0])

    assert low>=0
    assert high>=0

    for i in range(n-1):
        a,b = segments[i]
        c,d = segments[i+1]

        if b<c:
            low = max(low,c-b)
            high = max(high,d-a)
        elif d<a:
            low = max(low,a-d)
            high = max(high,b-c)
        else:
            high = max(high,abs(d-a),abs(b-c))

    # print(low,high)
    ans = -1
    while(low<=high):
        mid = (low+high)//2

        isFilled = tryFill(mid,segments)
        if isFilled:
            ans = mid
            high = mid-1
        else:
            low = mid+1
    print(ans)