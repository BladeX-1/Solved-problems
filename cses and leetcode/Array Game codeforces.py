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
import bisect
t = int(inputmethod())
for _ in range(t):
    n,k = [*map(int,inputmethod().split())]
    arr = [*map(int,inputmethod().split())]
    if k>=3:
        print(0)
        continue

    if k==0:
        print(min(arr))
        continue
    if k>=1:
        arr.sort()
        arrMin = arr[0]
        temp = arrMin
        for i in range(n-1):
            if arr[i+1]-arr[i]<temp:
                temp = arr[i+1]-arr[i]

        if k==1:
            print(temp)
            continue
        elif k==2:
            for ai in range(n):
                for bi in range(ai+1,n):
                    diff = arr[bi]-arr[ai]
                    cir = bisect.bisect_left(arr,diff)
                    cil = max(0,cir-1)
                    temp = min(temp,abs(diff-arr[cir]),abs(diff-arr[cil]))
            print(temp)