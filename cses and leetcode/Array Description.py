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


sys.setrecursionlimit(101000)

n,m = [*map(int,inputmethod().split(' '))]
arr = [*map(int,inputmethod().split(' '))]


for i in range(n-1):
    # if already existing adjecent numbers have difference greater than 1
    if arr[i]!=0 and arr[i+1]!=0 and abs(arr[i]-arr[i+1])>1:
        print(0)
        exit()

M = 10**9+7

from collections import defaultdict as dd
from collections import Counter



mat = [[0]*m for _ in range(m)]
matDict = dd(dd)
for i in range(m):
    mat[i][i] = 1
    matDict[i][i] = 1
    if i+1<m:
        mat[i][i+1] = 1
        matDict[i][i+1] = 1
    if i-1>=0:
        mat[i][i-1] = 1
        matDict[i][i-1] = 1

def matMul(a,b):
    c = [[0]*len(b[0]) for _ in range(len(a))]

    for row in range(len(a)):
        for col in range(len(b[0])):
            for i in range(len(a[0])):
                c[row][col] += (a[row][i]*b[i][col])%M
                c[row][col] %=M
    return c

def matMulDict(a,b):
    c = dd(dd)

    for ay in a:
        for ax in a[ay]:
            av = a[ay][ax]
            for bx in b[ax]:
                if bx in b[ax]:
                    bv = b[ax][bx]
                    c[ay][bx] += av+bv
                    c[ay][bx]%=M
    
    return c

def matPowerDict(a,p):
    assert p>=1
    if p==1:
        return a
    half = matPowerDict(a,p//2)
    if p%2==0:
        return matMulDict(half,half)
    else:
        return matMulDict(matMulDict(half,half),a)

def matPower(a,p):
    assert p>=1
    if p==1:
        return a
    half = matPower(a,p//2)
    if p%2==0:
        return matMul(half,half)
    else:
        return matMul(matMul(half,half),a)



aReach = dd(list)

import math
def zero(k):
    if k==0:
        return 1
    if k==1:
        return m

    # if m*k>=m**3*math.log2(k):
    p = matPower(mat,k-1)
    ans = 0
    for row in p:
        ans+=sum(row)%M
        ans%=M
    return ans
        
# m**3 * log(n)
# m*n


def single(a,k):
    if k==0:
        return 1

    if m*k>=m**3*math.log2(k):
        p = matPower(mat,k)
        ans = 0
        for y in range(m):
            ans+=p[y][a-1]
        return ans

    if k==0:
        return 1
    a = min(a,m-a+1)
    maxReach = a+k
    minReach = a-k

    if 1<=minReach and maxReach<=m:
        a+=-minReach+1
        

    if a not in aReach:
        c = Counter()
        if a-1>=1:
            c[a-1]+=1
        if a+1<=m:
            c[a+1]+=1

        c[a]+=1
        aReach[a].append(c)

    i = 1
    while(len(aReach[a])<k):
        lastC = aReach[a][-1]
        newC = lastC.copy()
        for ky,f in lastC.items():
            if ky-1>=1:
                newC[ky-1]+=f
                newC[ky-1]%=M
            if ky+1<=m:
                newC[ky+1]+=f
                newC[ky+1]%=M
        aReach[a].append(newC)
        i+=1

    return sum(aReach[a][k-1].values())


def double(a,b,k):
    if k==0:
        return 1

    if m*k>=m**3*math.log2(k):
        p = matPower(mat,k+1)
        return p[b-1][a-1]
    
    a,b = min(a,b),max(a,b)
    if m-b+1<a:
        a,b = m-b+1,m-a+1

    minReach = a-k
    maxReach = a+k

    if not(minReach-1<=b<=maxReach+1):
        return 0
    
    if a not in aReach:
        c = Counter()
        if a-1>=1:
            c[a-1]+=1
        if a+1<=m:
            c[a+1]+=1

        c[a]+=1
        aReach[a].append(c)

    i = 1
    while(len(aReach[a])<k+1):
        lastC = aReach[a][-1]
        newC = lastC.copy()
        for ky,f in lastC.items():
            if ky-1>=1:
                newC[ky-1]+=f
                newC[ky-1]%=M
            if ky+1<=m:
                newC[ky+1]+=f
                newC[ky+1]%=M
        aReach[a].append(newC)
        i+=1

    return aReach[a][k][b]


starts = []
ends = []
for i in range(n):
    # capture start, either i==0, or first zero
    if arr[i]==0 and (i==0 or arr[i-1]!=0):
        starts.append(i)
    if arr[i]==0 and (i==n-1 or arr[i+1]!=0):
        ends.append(i)

ans = 1
if len(starts)==0:
    print(1)
    exit()

if starts[0]==0 and ends[0]==n-1: # everything is zero
    temp = zero(n)
    ans*=temp
    ans%=M
    print(ans)
    exit()

if starts[0]==0:
    ans*=single(arr[ends[0]+1],ends[0]-starts[0]+1)
    ans%=M

    starts.pop(0)
    ends.pop(0)

    if len(starts)==0:
        print(ans)
        exit()

if ends[-1]==n-1:
    ans*=single(arr[starts[-1]-1],ends[-1]-starts[-1]+1)
    ans%=M
    starts.pop(-1)
    ends.pop(-1)

    if len(starts)==0:
        print(ans)
        exit()

# print(ans)
for i in range(len(starts)):
    ans*=double(arr[starts[i]-1],arr[ends[i]+1],ends[i]-starts[i]+1)
    ans%=M

print(ans)