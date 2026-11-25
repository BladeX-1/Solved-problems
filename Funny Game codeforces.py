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


def connect(dsu,a,b):
    aes = []
    pa = a
    while(dsu[pa]!=pa):
        aes.append(pa)
        pa = dsu[pa]

    bes = []
    pb = b
    while(dsu[pb]!=pb):
        bes.append(pb)
        pb = dsu[pb]


def find(dsu,a):
    p = a
    while(dsu[p]!=p):
        p = dsu[p]
    return p
    

from collections import defaultdict as dd
import itertools
import bisect

t = int(inputmethod())
for _ in range(t):
    n = int(inputmethod())
    arr = [*map(int,inputmethod().split(' '))]
    
    dsu = [*range(n+1)] # take 0 to n

    x2pairs = dict()
    isSolvable = True
    for x in range(2,n):
        mod2i = dd(list)
        for i in range(n):
            mod2i[arr[i]%x].append(i)

        pairs = list()

        for _mod,modValues in mod2i.items():
            # for a,b in itertools.combinations(modValues,2):
                # pairs.add((min(a,b),max(a,b)))
            pairs.append(modValues)

        if len(pairs)==0:
            print('NO')
            isSolvable = False
            break

        x2pairs[x] = pairs

    if not isSolvable:
        continue


    