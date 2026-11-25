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

ylen,xlen = [*map(int,inputmethod().split())]
color2y = dd(list)
color2x = dd(list)
for y in range(ylen):
    row = [*map(int,inputmethod().split())]
    for x in range(xlen):
        color2y[row[x]].append(y)
        color2x[row[x]].append(x)

ans = 0
for c in color2x:
    ys = color2y[c]
    ys.sort()

    xs = color2x[c]
    xs.sort()

    sumYX = [0]*len(ys)
    for i in range(len(ys)):
        sumYX[i] = ys[i]+xs[i]

    for i in range(len(sumYX)):
        left = i
        right = len(sumYX)-1-i
        ans+=(left-right)*sumYX[i]

print(ans)