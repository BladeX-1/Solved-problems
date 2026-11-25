import sys
inputI_23235231253 = -1
inputArr_6273468273 = []
spliter = "\n"
try:
    open("__localsystemflag__").close()
    file_input_txt_2342349 = open('inp.txt')
    env = 'local'
except FileNotFoundError:
    rawInput = sys.stdin.read()
    inputArr_6273468273 = rawInput.splitlines()
    
    inputI_23235231253 = 0
    file_input_txt_2342349 = None
    env = 'server'

def inputmethod():
    global inputI_23235231253
    if file_input_txt_2342349:
        return file_input_txt_2342349.readline().strip()
    else:
        inputI_23235231253+=1
        return inputArr_6273468273[inputI_23235231253-1]
        return input()



lenArr,lenBrr,q = [*map(int,inputmethod().split())]
arr = [*map(int,inputmethod().split())]
brr = [*map(int,inputmethod().split())]

A = sum(arr)
B = sum(brr)

biB = set()
for bi in brr:
    biB.add(bi-B)

aiA = set()
for aA in arr:
    aiA.add(aA-A)

import math
from collections import defaultdict as dd

primes = [2]
for p in range(3,int(math.sqrt(2*10**5))+1,2): # O(n**0.5)
    isPrime = True
    sqrtP = int(math.sqrt(p))
    for px in primes: # O(n**0.5/0.5/log(n))
        if px>sqrtP:
            break
        if px%p==0:
            isPrime = False
            break

    if isPrime:
        primes.append(p)

def getHalfDivisors(factors,keys,i,temp,full,sqrtX):
    if i==len(keys):
        full.append(temp)
        return

    for f in range(factors[keys[i]]+1):
        if temp*(keys[i]**f)>sqrtX:
            break
        getHalfDivisors(factors,keys,i+1,temp*(keys[i]**f),full,sqrtX)

import time

for _ in range(q):
    x = int(inputmethod())
    sign = x//abs(x)
    x*=sign
    xCopy = x
    
    factors = dd(int)

    for p in primes:
        sqrtX = int(math.sqrt(x))
        if p>sqrtX:
            break
        while(x%p==0):
            factors[p]+=1
            x//=p
        
    if x!=1:
        factors[x]+=1

    divisors = []
    getHalfDivisors(factors,list(factors.keys()),0,1,divisors,int(math.sqrt(xCopy)))
    # divisors.sort()

    isSolved = False
    sqrtX = int(math.sqrt(xCopy))
    for f1 in divisors:
        assert xCopy%f1==0
        # if f1>sqrtX:
        #     break
        f2 = xCopy//f1

        f1*=sign
        if (f1 in aiA and f2 in biB) \
            or (f2 in aiA and f1 in biB) \
            or (-f1 in aiA and -f2 in biB) \
            or (-f2 in aiA and -f1 in biB):
            isSolved = True
            break

    if isSolved:
        print("YES")
    else:
        print("NO")