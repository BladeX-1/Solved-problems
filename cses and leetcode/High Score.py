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

inf=float('inf')
from collections import defaultdict as dd
n,edges = [*map(int,inputmethod().split(' '))]
adj = dd(lambda:dd(lambda:inf))
revAdj = dd(list)
for _ in range(edges):
    a,b,w = [*map(int,inputmethod().split(' '))]
    adj[a-1][b-1] = min(-w,adj[a-1][b-1])
    revAdj[b-1].append(a-1)

# bellman ford
distances = [float('inf')]*n
distances[0] = 0
inf=float('inf')
cycles = set()
for i in range(n):
    for a in range(n):
        for b in adj[a]:
            w = adj[a][b]
            if distances[a]!=inf and distances[b]>distances[a]+w:
                if i==n-1:
                    cycles.add(b)
                distances[b] = distances[a]+w


def graph_bfs(adj, i, addedToQue):
    q = [i]
    addedToQue.add(i)
    while q:
        top = q.pop(0)
        for near in adj[top]:
            if near in addedToQue:
                continue
            addedToQue.add(near)
            q.append(near)

if cycles:
    allFromStart = set()
    graph_bfs(adj,0,allFromStart)

    fromAllToEnd = set()
    graph_bfs(revAdj,n-1,fromAllToEnd)

    common = (allFromStart&fromAllToEnd&cycles)
else:
    common = set()

if common:
    print(-1)
else:
    print(-distances[-1])
