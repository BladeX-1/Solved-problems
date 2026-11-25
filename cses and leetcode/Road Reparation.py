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


from collections import defaultdict as dd

n,m = [*map(int,inputmethod().split(' '))]
# adj = [dd() for _ in range(n)]
edges = []
for _ in range(m):
    a,b,p = [*map(int,inputmethod().split(' '))]
    # assert a-1 not in adj or b-1 not in adj[a-1],  "parallel edges detected"
    # adj[a-1][b-1] = p
    # adj[b-1][a-1] = p
    edges.append([a-1,b-1,p])

from collections import deque
import heapq

dsu = [*range(n)]
def add(a,b):
    aes = []
    p = a
    while(dsu[p]!=p):
        aes.append(p)
        p = dsu[p]
    aes.append(p)

    bes = []
    p = b
    while(dsu[p]!=p):
        bes.append(p)
        p = dsu[p]
    bes.append(p)

    assert dsu[aes[-1]]!=dsu[bes[-1]]
    
    if len(aes)>len(bes):
        for i in aes:
            dsu[i] = dsu[bes[-1]]
    else:
        for i in bes:
            dsu[i] = dsu[aes[-1]]
    
def find(x):
    p = x
    while(p!=dsu[p]):
        p = dsu[p]

    return p

import heapq
def kruskal():
    q = []
    for a,b,p in edges:
        heapq.heappush(q,[p,a,b])

    ans = 0
    while(q):
        p,a,b = heapq.heappop(q)
        if find(a)!=find(b):
            ans+=p
            add(a,b)

    return ans

selfRefCount = 0
ans = kruskal()
for i in range(n):
    if dsu[i]==i:
        selfRefCount+=1

if selfRefCount>1:
    print("IMPOSSIBLE")
else:
    print(ans)