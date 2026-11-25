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

n,edges = [*map(int,inputmethod().split(' '))]
adj = dd(dd)
adjRev = dd(list)
edgeList = []
for _ in range(edges):
    a,b,w = [*map(int,inputmethod().split(' '))]
    adj[a-1][b-1] = min(w,adj[a-1].get(b-1,float('inf')))
    adjRev[b-1].append((a-1,b-1))
    assert a!=b

distance = [float('inf')]*n
distance[0] = 0
inf=float('inf')
cycleNodes = []
# bellman ford
for i in range(n):
    for a in adj:
        for b,w in adj[a].items():
            if distance[a]!=inf and distance[a]+w<distance[b]:
                if i==n-1:
                    cycleNodes.append(b)
                    break
                distance[b] = distance[a]+w


# 0: unvisited     1: exploring   2: finished
def graph_dfs(adj, i, visited, path, reach, currentReach):
    path.append(i)
    visited[i] = 1
    reach[i] = currentReach
    for near,nearWeight in adj[i]:
        if near in visited:
            if visited[near]==1 and currentReach-reach[near]<0:
                path.append(near)
                return path
            else:
                # either forward edge or cross
                continue
        
        possiblePath = graph_dfs(adj, near, visited, path, reach, currentReach+nearWeight)
        if possiblePath:
            return possiblePath
    path.pop(-1)
    visited[i] = 2
    return []

if not cycleNodes:
    print("NO")
else:
    print("YES")
    path = graph_dfs(adjRev,cycleNodes[0],dict(),[],dict(),0)
    i = path.index(path[-1])
    path = path[i:]
    print(*map(lambda x:x+1,path))