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


import heapq
from collections import defaultdict as dd
n,m,q = [*map(int,inputmethod().split(' '))]
adj = dd(dd)
for _ in range(m):
    a,b,w = map(int,inputmethod().split(' '))
    if a-1 not in adj or b-1 not in adj[a-1]:
        adj[a-1][b-1] = w
        adj[b-1][a-1] = w
    else:
        adj[a-1][b-1] = min(w,adj[a-1][b-1])
        adj[b-1][a-1] = min(w,adj[a-1][b-1])

def graph_bfs(adj, i, n):
    popped = set()

    distances = [float('inf')]*n
    q = [(0,i)]
    distances[0] = 0
    while q:
        topDis,top = heapq.heappop(q)
        if top in popped:
            continue
        popped.add(top)
        if len(popped)==n:
            break
        for near in adj[top]:
            nearDis = adj[top][near]
            if near in popped:
                continue
            if distances[near]>nearDis+topDis:
                distances[near] = nearDis+topDis
                heapq.heappush(q,(nearDis+topDis,near))
    ans = [(x if x!=float('inf') else -1) for x in distances]
    assert len(ans)==n
    return ans


allPairDistance = []
for i in range(n):
    allPairDistance.append(graph_bfs(adj,i,n))
    print(i)

answers = []
for _ in range(q):
    a,b = map(int,inputmethod().split(' '))
    answers.append(str(allPairDistance[a-1][b-1]))

print('\n'.join(answers))