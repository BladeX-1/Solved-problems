try:
    open("__localsystemflag__").close()
    f = open('inp.txt')
    env = 'local'
except FileNotFoundError:
    f = None
    env = 'server'

def inputmethod():
    if f:
        return f.readline().strip()
    else:
        return input()
    
n, trapsCount = [*map(int,inputmethod().split(' '))]
traps = set()
for _ in range(trapsCount):
    y,x = [*map(int,inputmethod().split(' '))]
    traps.add((y,x))

from collections import defaultdict as dd

grid = dd(int)
grid[(0,0)] = 1
M = 10**9+7

fact = [1]
for i in range(1,2*n+1):
    fact.append((fact[-1]*i)%M)

def C(n,r):
    ncr = (fact[n]*pow(fact[r],-1,M)*pow(fact[n-r],-1,M))%M
    print("ncr",n,r,ncr)
    return ncr

def f(n,r):
    ans = C(n+r-2,r-1)
    print('f',n,r,ans)
    return ans



ans = f(n,n)
for y,x in traps:
    ans-=f(n+1-y,n+1-x)

ans+=M
ans%=M

print(ans)