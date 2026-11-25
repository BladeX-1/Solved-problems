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



primes = [2]
x = 3
import math
upper = math.ceil((10**9)**(0.5))
while(x<=upper):
    sqrtX = math.floor(math.sqrt(x))
    if sqrtX**2==x:
        x+=2
        continue
    for p in primes:
        if p>sqrtX:
            primes.append(x)
            break
        elif x%p==0:
            break
    x+=2

primeSet = set(primes)

from collections import defaultdict as dd

t = int(inputmethod())
for _ in range(t):
    n = int(inputmethod())

    if n%2==0:
        print(n//2,n//2)
        continue
    if n in primeSet:
        print(1,n-1)
        continue

    factor = n
    sqrtN = math.floor(math.sqrt(n))
    for p in primes:
        if n%p==0:
            factor=p
            break
        if p>sqrtN:
            break

            
    if factor==n:
        print(1,n-1)
        continue

    x = factor
    print(1*n//x,(x-1)*n//x)