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

import itertools
from collections import defaultdict as dd
from collections import Counter

M = 10**9+7
t = int(inputmethod())
for _ in range(t):
    n,k = [*map(int,inputmethod().split())]
    arr = [*map(int,inputmethod().split())]

    ands = 2**7-1
    for i in range(n):
        ands&=arr[i]

    if ands.bit_count()>0:
        k-=ands.bit_count()

        for i in range(n):
            arr[i]&=~ands
    
    counter = Counter(arr)

    arrSet = set(arr)
    arr = list(arrSet)
    n = len(arr)

    ithBitSetFor = [set() for _ in range(7)]

    for i in range(n):
        temp = arr[i]
        for j in range(7):
            if temp>>j == 0:
                break
            if (temp>>j)&1 == 1:
                ithBitSetFor[j].add(arr[i])

    ans = 0
    for i in range(0,64):
        if i.bit_count()!=k:
            continue

        tempOnes = arrSet
        tempZeros = arrSet
        for j in range(7):
            if (i>>j)&1==1:
                tempOnes &= ithBitSetFor[j]
            elif (i>>j)&1==0:
                tempZeros &= arrSet-ithBitSetFor[j]

        fSum = 0
        for j in tempOnes:
            fSum+=counter[j]

        ans+=pow(2,fSum,M)-1
        ans%=M

    print(ans)