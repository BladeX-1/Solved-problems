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



n, edges = [*map(int,input().split(' '))]
from collections import defaultdict as dd
adj = dd(dd)

for _ in range(edges):
    a,b,p = [*map(int,input().split(' '))]
    assert a-1 not in adj or b-1 not in adj[a-1]
    adj[a-1][b-1] = p

def graph_bfs(adj, i, n):
    import heapq
    poppedToQue = set()

    distances = [float('inf')]*n
    q = [(0,i)]
    while q:
        top,topDis = heapq.heappop(q)
        distances[top] = topDis
        if top in poppedToQue:
            continue
        poppedToQue.add(top)

        for near in adj[top]:
            if near in poppedToQue:
                continue
            p = adj[top][near]
            heapq.heappush(q,(topDis+p,near))

    return distances

distances = graph_bfs(adj,0,n)
