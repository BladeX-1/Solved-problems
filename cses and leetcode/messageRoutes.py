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
from collections import deque
def graph_bfs(adj,n):
    addedToQue = set()

    parent = [-1]*n

    q = deque([0,None])
    addedToQue.add(0)
    dis = 1
    while len(q)>1:
        top = q.popleft()
        if top is None:
            dis+=1
            q.append(None)
            continue

        for near in adj[top]:
            if near in addedToQue:
                continue
            parent[near] = top
            addedToQue.add(near)
            if near==n-1:
                break

            q.append(near)


    if parent[n-1]==-1:
        return -1,[]
    chain = []
    i = n-1
    while(i!=-1):
        chain.append(i+1)
        i = parent[i]

    chain.reverse()
    return len(chain),chain


nodes,edges = [*map(int,inputmethod().split(' '))]

adj = dd(list)
for _ in range(edges):
    a,b = [*map(int,inputmethod().split(' '))]
    adj[a-1].append(b-1)
    adj[b-1].append(a-1)

dis,parent = graph_bfs(adj,nodes)
if dis==-1:
    print("IMPOSSIBLE")
else:
    print(dis)
    print(*parent)