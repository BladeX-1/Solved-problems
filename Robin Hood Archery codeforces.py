import sys
inputI = -1
inputArr = []
spliter = "\n"
try:
    open("__localsystemflag__").close()
    f = open('inp.txt')
    out = open("out.txt")
    env = 'local'
except FileNotFoundError:
    rawInput = sys.stdin.read()
    inputArr = rawInput.splitlines()
    
    inputI = 0
    f = None
    out = None
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
import bisect
t = int(inputmethod())
for _ in range(t):
    n,q = [*map(int,inputmethod().split())]
    arr = [*map(int,inputmethod().split())]

    x2is = dd(list)
    for i in range(n):
        x2is[arr[i]].append(i)

    cumuXor = [0]
    for x in arr:
        cumuXor.append(cumuXor[-1]^x)

    for _q in range(q):
        l,r = [*map(int,inputmethod().split())]
        l-=1
        r-=1
        intervalSize = r-l+1
        if intervalSize%2==1:
            print("NO")
            continue

        if arr[l]==arr[r]:
            ies = x2is[arr[r]]
            li = bisect.bisect_left(ies,l)
            ri = bisect.bisect_left(ies,r)
            if ri-li+1==intervalSize:
                print('YES')
                continue

        

        
        