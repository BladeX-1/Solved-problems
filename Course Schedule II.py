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
adj = [set() for _ in range(n)]

inDegree = [0]*n
for _ in range(m):
    a,b = [*map(int,inputmethod().split(' '))]
    if (b-1) not in adj[a-1]:
        adj[a-1].add(b-1)
        inDegree[b-1]+=1

heap = []
added = set()
for i in range(n):
    if inDegree[i]==0:
        heap.append(i)
        added.add(i)

ans = []
import heapq

heapq.heapify(heap)

while(heap):
    t = heapq.heappop(heap)
    ans.append(t)
    for near in adj[t]:
        inDegree[near] -= 1
        if inDegree[near] == 0:
            heapq.heappush(heap,near)

assert len(ans)==n,f"{len(ans)=} {n=}"
print(*map(lambda x:x+1,ans))