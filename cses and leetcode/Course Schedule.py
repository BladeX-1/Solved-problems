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


from collections import deque
def topo(adj, n):
    # def graph_bfs(grid,y,x):
    # addedToQue = set()
    indegree = [0]*n
    for a in adj:
        for b in adj[a]:
            indegree[b]+=1

    q = deque()
    for i in range(n):
        if indegree[i]==0:
            q.append(i)
    topo = []
    while(q):
        top = q.popleft()
        topo.append(top)

        for near in adj[top]:
            indegree[near]-=1
            if indegree[near]==0:
                q.append(near)

    if len(topo)<n:
        return []
    return topo

from collections import defaultdict as dd
n,m = [*map(int,inputmethod().split(' '))]
adj = dd(list)
for _ in range(m):
    a,b = [*map(int,inputmethod().split(' '))]
    adj[a-1].append(b-1)

ans = topo(adj,n)
if ans:
    print(*map(lambda x:x+1,ans))
else:
    print('IMPOSSIBLE')