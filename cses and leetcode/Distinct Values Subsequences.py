import sys
inputI = -1
inputArr = []
try:
    open("__localsystemflag__").close()
    f = open('inp.txt')
    env = 'local'
except FileNotFoundError:
    inputArr = sys.stdin.read().split('\n')
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



n = int(inputmethod())
arr = [*map(int,inputmethod().split(' '))]

from collections import Counter
c = Counter(arr)

ans = 1
M = 10**9+7
for x,f in c.items():
    ans*=(f+1)
    ans%=M

ans-=1
ans%=M
print(ans)