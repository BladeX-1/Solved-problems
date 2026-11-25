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

M = 10**9+7
def modFact(n,M):
    ans = 1
    for i in range(1,n+1):
        ans*=i
        ans%=M
    return ans

from collections import Counter
t = int(inputmethod())
for _ in range(t):
    n = int(inputmethod())
    arr = [*map(int,inputmethod().split())]
    arrCounter = Counter(arr)
    cumuAnd = arr[0]
    for i in range(1,n):
        cumuAnd&=arr[i]

    if arrCounter[cumuAnd]<2:
        print(0)
        continue

    ans = 1
    ans*=arrCounter[cumuAnd]*(arrCounter[cumuAnd]-1)

    ans*=modFact(n-2,M)
    ans%=M
    print(ans)