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


import heapq
from collections import defaultdict as dd

n,m = [*map(int,inputmethod().split(' '))]
adj = dd(dd)

for _ in range(m):
    a,b,w = [*map(int,inputmethod().split(' '))]
    # assert a-1 not in adj or b-1 not in adj[a-1], "graph contains multiple edges between same two nodes"
    if a-1 in adj and b-1 in adj[a-1]:
        adj[a-1][b-1] = min(adj[a-1][b-1],w)
    else:
        adj[a-1][b-1] = w

from collections import deque
def graph_bfs(adj,n):
    q = [[0,0,0,0]]
    inf=float('inf')
    bestPrice = [inf]*n
    bestPrice[0] = 0
    pathPrice = [inf]*n
    pathPrice[0] = 0

    while q:
        topPrice,topBest,topPathMax,top = heapq.heappop(q)
        if pathPrice[top]<topPrice and bestPrice[top]<topBest:
            continue

        for near in adj[top]:
            nearPrice = adj[top][near]
            nearPathMax = max(topPathMax,nearPrice)
            shouldPush = False
            if topPrice+nearPrice<pathPrice[near]:
                pathPrice[near] = topPrice+nearPrice
                shouldPush = True
            if topPrice+nearPrice-(nearPathMax+1)//2 < bestPrice[near]:
                bestPrice[near] = topPrice+nearPrice-(nearPathMax+1)//2
                shouldPush = True
            if near!=n-1 and shouldPush:
                heapq.heappush(q,[topPrice+nearPrice,topPrice+nearPrice-(nearPathMax+1)//2,nearPathMax,near])

    return bestPrice[-1]


ans = graph_bfs(adj,n)
print(ans)