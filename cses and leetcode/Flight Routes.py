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
n,m,k = [*map(int,inputmethod().split(' '))]
adj = [[] for _ in range(n)]
for _ in range(m):
    a,b,w = [*map(int,inputmethod().split(' '))]
    adj[a-1].append((b-1,w))

import heapq
def graph_bfs(adj,n,k):
    # def graph_bfs(grid,y,x):
    popped = dd(int)

    start = 0
    end = n-1
    q = [(0,start)]
    ans = []
    while q:
        topPrice,top = heapq.heappop(q)
        popped[top] += 1
        if top==end:
            ans.append(topPrice)
            if len(ans)==k:
                break
        for near,nearPrice in adj[top]:
            if popped[near]>=k:
                continue
            heapq.heappush(q,(nearPrice+topPrice,near))

    return ans

ans = graph_bfs(adj,n,k)
print(*ans)