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

primes = []
for i in range(3,math.floor(math.sqrt(10**9))+50,2):
    sqrtI = math.floor(math.sqrt(i))
    isPrime = True
    for p in primes:
        if p>sqrtI:
            break
        if i%p==0:
            isPrime = False
            break
    if isPrime:
        primes.append(i)


primes = [2]+primes

from collections import defaultdict as dd

t = int(inputmethod())
for _ in range(t):
    n = int(inputmethod())
    factors = dd(int)

    tempN = n
    for p in primes:
        if p>math.sqrt(tempN):
            if tempN>1:
                factors[tempN]+=1
                tempN = 1
            break
        while(tempN%p==0):
            factors[p]+=1
            tempN//=p

    if tempN>1:
        factors[tempN]+=1
        tempN = 1

    # print('factors',factors)
    # print(n,factors)
    keys = list(factors.keys())
    if len(factors)>=3:
        a = keys[0]**factors[keys[0]]
        b = keys[1]**factors[keys[1]]
        c = 1
        for i in range(2,len(keys)):
            c*= keys[i]**factors[keys[i]]

        assert a*b*c==n
        print("YES")
        print(a,b,c)

    elif len(factors)==2:
        count1 = factors[keys[0]]
        count2 = factors[keys[1]]

        if count1>=2 and count2>=2:
            a = keys[0]**(count1-1)
            b = keys[0]*keys[1]
            c = keys[1]**(count2-1)
            assert a*b*c==n
            
            print("YES")
            print(a,b,c)

        elif count1>=3:
            a = keys[0]
            b = keys[0]**2
            c = keys[1]**count2*keys[0]**(count1-3)
            assert a*b*c==n
            print("YES")
            print(a,b,c)
        elif count2>=3:
            a = keys[1]
            b = keys[1]**2
            c = keys[0]**count1*keys[1]**(count2-3)
            assert a*b*c==n
            print("YES")
            print(a,b,c)

        else:
            print('NO')
            continue
    elif len(factors)==1:
        if factors[keys[0]]<=5:
            print("NO")
            continue
        else:
            a = keys[0]
            b = keys[0]**2
            c = keys[0]**(factors[keys[0]]-3)
            assert a*b*c==n

            print("YES")
            print(a,b,c)
    else:
        assert False