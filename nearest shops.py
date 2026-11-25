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



n,m,k = [*map(int,inputmethod().split(' '))]
animeShops = [*map(lambda x:x-1,map(int,inputmethod().split(' ')))]
animeShops = set(animeShops)
adj = [set() for _ in range(n)]
for _ in range(m):
    a,b = [*map(int,inputmethod().split(' '))]
    adj[a-1].add(b-1)
    adj[b-1].add(a-1)

from collections import deque
def graph_bfs_rev(adj, anime, n):
    q = deque()
    putInQue = set()
    for a in anime:
        q.append((0,a,a))
        # putInQue.add(a)

    distance = [-1]*n
    filled = 0
    while q:
        topDis,top,topHead = q.popleft()
        for near in adj[top]:
            if near==topHead:
                continue
            if near in putInQue:
                continue
            putInQue.add(near)
            distance[near] = topDis+1
            q.append((topDis+1,near,topHead))

    return distance

ans = graph_bfs_rev(adj,animeShops,n)
# print(*map(lambda x:x,ans))
print(*ans)