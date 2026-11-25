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
import time

cities, roads = [*map(int,inputmethod().split(' '))]
adj = dd(list)
for _ in range(roads):
    a,b = [*map(int,inputmethod().split(' '))]
    adj[a].append(b)
    adj[b].append(a)


def graph_dfs(adj, i, visited):
    for near in adj[i]:
        if near in visited:
            continue
        visited.add(near)
        graph_dfs(adj, near, visited)

def graph_bfs(adj, i, addedToQue):

    q = [i]
    while q:
        top = q.pop(0)
        for near in adj[top]:
            if near in addedToQue:
                continue
            addedToQue.add(near)
            q.append(near)

components = 0
visitedGlobal = set()
clusters = []
if env=='local':
    t = time.time()
for i in range(1,cities+1):
    if i in visitedGlobal:
        continue
    components+=1
    visited = set()
    visited.add(i)
    graph_bfs(adj,i,visited)
    visitedGlobal.update(visited)
    clusters.append(visited)


arr = [str(components-1)]
for i in range(len(clusters)-1):
    x = None
    for x in clusters[i]:
        break
    
    y = None
    for y in clusters[i+1]:
        break

    arr.append(f"{x} {y}")

print('\n'.join(arr))
if env=="local":
    print(time.time()-t)