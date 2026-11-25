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



n,a,b = [*map(int,inputmethod().split(' '))]

from fractions import Fraction
from decimal import Decimal

fact = [1]
for i in range(1,600+1):
    fact.append(fact[-1]*i)


def C(n,r):
    return Fraction(fact[n],fact[r]*fact[n-r])

def f(k):
    ## (x(1-x**6)/(1-x))**n
    ## x**n * (1-x**6)**n * (SUM:T(i)x**i)
    ## T(i) = C(n+i-1,i)
    ## for (1-x**6)**n, it is made of SUM:C(n,r) * (-1)**r * x**(6n)
    
    # for first term
    k-=n


    i = 0
    ans = 0
    while(k-6*i>=0):
        ans += C(n,i)*((-1)**i)*C(n+k-6*i-1,k-6*i)
        i+=1
    return ans

ans = 0
for i in range(a,b+1):
    ans+=f(i)
# print(ans,6**n)
# for _ in range(n):
ans/=6**n
# print(ans)


ans = round(float(ans),6)
s = f"{ans:6f}"
print(s)