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

from collections import defaultdict as dd
n, edges = [*map(int,inputmethod().split(' '))]
adj = dd(list)
for _ in range(edges):
    a,b,weight = map(int,inputmethod().split(' '))
    adj[a-1].append((b-1,weight))


import heapq
def graph_bfs(adj, i, n):
    addedToQue = set()

    allDistance = [float('inf')]*n
    q = [(0,i)]
    allDistance[0] = 0
    while q:
        topDis, top = heapq.heappop(q)

        if top in addedToQue:
            continue
        addedToQue.add(top)

        allDistance[top] = topDis

        for near,nearEdge in adj[top]:
            if near in addedToQue:
                continue


            heapq.heappush(q,(topDis+nearEdge,near))

    return allDistance

allDistances = graph_bfs(adj,0,n)
print(*allDistances)