import math


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


t = int(inputmethod())

maxN = 10**7+1
i2iSquare = dict()
for i in range(0,math.ceil(math.sqrt(maxN))):
    i2iSquare[i]=i*i

sumTwoSquares2num = dict()
for i,iSq in i2iSquare.items():
    for j,jSq in i2iSquare.items():
        sumTwoSquares2num[iSq+jSq] = (i,j)

for _ in range(t):
    n = int(inputmethod())
    for sumTwoSq in sumTwoSquares2num:
        remaining = n-sumTwoSq
        if remaining in sumTwoSquares2num:
            print(*sumTwoSquares2num[sumTwoSq],*sumTwoSquares2num[remaining])
            break