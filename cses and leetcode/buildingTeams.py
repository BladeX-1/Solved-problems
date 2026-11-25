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
adj = dd(list)
for _ in range(edges):
    a,b = [*map(int,inputmethod().split(' '))]
    adj[a-1].append(b-1)
    adj[b-1].append(a-1)

colors = [-10]*n

allColors = {0,1}
from collections import deque
def graph_bfs(adj, i, colors):

    addedToQue = set()
    possible = True

    for i in range(n):
        if i in addedToQue:
            continue
        q = deque([i,None])
        addedToQue.add(i)
        color = 0
        colors[i] = color
        possible = True
        while len(q)>1:
            top = q.popleft()
            if top is None:
                q.append(None)
                color^=1
                continue

            for near in adj[top]:
                if near in addedToQue:
                    assert colors[near] != -10
                    if colors[near] == color^1:
                        continue
                    else:
                        possible = False
                        break

                colors[near] = color^1
                addedToQue.add(near)
                q.append(near)

            if not possible:
                break

    return possible


solved = graph_bfs(adj,0,colors)
if not solved:
    print("IMPOSSIBLE")
else:
    teams = [*map(lambda x:x+1,colors)]
    print(*teams)