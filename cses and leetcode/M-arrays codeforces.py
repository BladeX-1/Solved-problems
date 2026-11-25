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

from collections import Counter

t = int(inputmethod())
for _t in range(t):
    n,m = [*map(int,inputmethod().split())]
    arr = [*map(int,inputmethod().split())]

    if _t==1:
        pass

    arr2 = [*map(lambda x:x%m,arr)]

    c = Counter(arr2)

    ans = 0
    if c[0]>0:
        ans+=1
        del c[0]
    if m%2==0 and c[m//2]>0:
        ans+=1
        del c[m//2]


    for x1,f1 in (c.items()):
        x2 = m-x1
        
        if x2 not in c:
            ans+=f1
            continue
        if x2<x1:
            continue
        f2 = c[x2]
        assert x1!=0 and x1!=x2
        if max(f1,f2)<=1+min(f1,f2):
            ans+=1
        else:
            ans+=1
            ans+=max(f1,f2)-(min(f1,f2)+1)

    print(ans)