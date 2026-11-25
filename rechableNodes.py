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

OPEN = 0
CLOSED = 1
inf=float('inf')

n,v = map(int,inputmethod().split())
myReach = [0]*n
def graph_dfs(adj, i, visited):
    visited.add(i)
    for near in adj[i]:
        if near in visited:
            myReach[i]|=myReach[near]
            continue
        myReach[i]|=graph_dfs(adj,near,visited)
    myReach[i]|=1<<i
    return myReach[i]

def topo(adj, i, visited, revTopo):
    for near in adj[i]:
        if near in visited:
            continue
        visited.add(near)
        topo(adj, near, visited, revTopo)

    revTopo.append(i)

adj = [[] for _ in range(n)]
for _ in range(v):
    a,b = map(int,inputmethod().split())
    adj[a-1].append(b-1)


import sys

sys.setrecursionlimit(10**5)

visited = set()
revTopo = []
for i in range(n):
    if i not in visited:
        visited.add(i)
        topo(adj,i,visited,revTopo)


visited = set()
topoList = [*reversed(revTopo)]
# topoList = revTopo
for i in reversed(topoList):
    if i not in visited:
        graph_dfs(adj, i, visited)

print(*map(lambda x:x.bit_count(),myReach))