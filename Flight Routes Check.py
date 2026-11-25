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


n,m = [*map(int,inputmethod().split(' '))]
adj = [[] for _ in range(n)]
reachHereFrom = [set() for _ in range(n)]
for _ in range(m):
    a,b = [*map(int,inputmethod().split(' '))]
    adj[a-1].append(b-1)


from collections import deque
def graph_bfs(adj, i, n):
    addedToQue = set()

    q = deque([i])
    addedToQue.add(i)
    while q:
        top = q.popleft()
        for near in adj[top]:
            if near in addedToQue:
                continue
            addedToQue.add(near)
            q.append(near)

    return addedToQue

for i in range(n):
    reachFromI = graph_bfs(adj,i,n)
    if len(reachFromI)==n:
        continue
    else:
        print('NO')
        print(i,list(set(range(n))-reachFromI)[0])
        exit()
print("YES")