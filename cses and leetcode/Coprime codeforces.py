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


import math

t = int(inputmethod())
for _ in range(t):
    n = int(inputmethod())
    arr = [*map(int,inputmethod().split())]

    x2i = dict()
    for i in reversed(range(n)):
        if arr[i] in x2i:
            arr[i] = -1
        else:
            x2i[arr[i]] = i+1


    ans =-1
    for x1,i1 in x2i.items():
        for x2,i2 in x2i.items():
            if i1+i2>ans and math.gcd(x1,x2)==1:
                ans = i1+i2

    print(ans)