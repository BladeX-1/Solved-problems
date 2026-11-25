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


from collections import defaultdict as dd
t = int(input())
for _ in range(t):
    n,x,y = [*map(int,input().split())]
    arr = [*map(int,input().split())]

    mod2ix = dd(set)
    mod2iy = dd(set)


    for i in range(n):
        mod2ix[arr[i]%x].add(i)
        mod2iy[arr[i]%y].add(i)

    ans = 0
    for x1 in sorted(mod2ix.keys()):
        if (x-x1)%x not in mod2ix:
            continue

        x2 = (x-x1)%x
        if x2<x1:
            break
        setx1 = mod2ix[x1]
        setx2 = mod2ix[x2]

        for y1 in sorted(mod2iy.keys()):
            if (y1-y)%y not in mod2iy:
                continue
            y2 = (y-x1)%y
            if y2<y1:
                break
            sety1 = mod2iy[y1]
            sety2 = mod2iy[y2]

            s1 = setx1&sety1
            s2 = setx2&sety2

            s3 = s1-s2
            s4 = s2-s1

            ans+=l1*l2