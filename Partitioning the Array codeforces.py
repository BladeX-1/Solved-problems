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


primes = [2]
p = 3
import math
upper = 2*10**5
while(p<=upper):
    sqrtP = math.sqrt(p)
    isPrime = True
    for px in primes:
        if px>sqrtP:
            break
        if p%px==0:
            isPrime = False
            break
    if isPrime:
        primes.append(p)
    p+=2
primesSet = set(primes)
# print(primes[:100])

from collections import defaultdict as dd

def getFactors(factorise,keys,i,ansTemp,ans):
    if i==len(keys):
        ans.append(ansTemp)
        return

    for power in range(0,factorise[keys[i]]+1):
        getFactors(factorise,keys,i+1,ansTemp*(keys[i]**power),ans)

    

t = int(inputmethod())
for _ in range(t):
    n = int(inputmethod())
    arr = [*map(int,inputmethod().split())]

    ans = 0
    if n==1:
        print(1)
        continue

    ans+=1 ## for entire length, for 1 segment

    factorise = dd(int)
    tempN = n
    for p in primes:
        sqrtN = math.sqrt(tempN)
        if p>sqrtN:
            break
        while(tempN and tempN%p==0):
            factorise[p]+=1
            tempN//=p

    if tempN!=1:
        factorise[tempN]+=1

    factors = []
    getFactors(factorise,list(factorise.keys()),0,1,factors)
    factors.sort()
    factors.pop(-1)
    # if n!=1:
    #     factors.remove(1)

    # print(f"{len(factors)=} {factors=}")


    fci = 0
    while(fci<len(factors)):
        fc = factors[fci]
        tempArr = arr[:]
        for i in range(1,n//fc):
            for j in range(fc):
                tempArr[i*fc+j]-=tempArr[j]
                tempArr[i*fc+j] = abs(tempArr[i*fc+j])

        g = math.gcd(*tempArr[fc:])
        if g>1 or g==0:
            for i in reversed(range(fci,len(factors))):
                if factors[i]%fc==0:
                    del factors[i]
                    ans+=1
            continue
        fci += 1

    print(ans)