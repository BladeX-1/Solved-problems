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


nodes,edges = [*map(int,inputmethod().split(' '))]
from collections import defaultdict as dd
adj = dd(list)
for _ in range(edges):
    u,v = [*map(int,inputmethod().split(' '))]
    adj[u].append(v)

def graph_dfs(adj, i, visited,revTopo):
    for near in adj[i]:
        if near in visited:
            assert False, "Graph is not a DAG"
            continue
        visited.add(near)
        graph_dfs(adj, near, visited, revTopo)
    revTopo.append(i)

revTopo = []
visited = set()
for i in range(nodes,0,-1):
    if i in visited:
        continue
    visited.add(i)
    graph_dfs(adj,i,visited,revTopo)

revTopo.reverse()
print(*revTopo)