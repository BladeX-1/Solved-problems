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

def nc2(n):
    return (n*(n-1))//2

t = int(inputmethod())
for _ in range(t):
    n = int(inputmethod())
    arr = [*map(int,inputmethod().split())]
    arr2 = [*map(lambda e:e[1]-e[0],zip(range(n),arr))]

    c = Counter(arr2)

    ans = 0
    for k,v in c.items():
        ans+=nc2(v)

    print(ans)