import sys
inputI = -1
inputArr = []
try:
    open("__localsystemflag__").close()
    f = open('inp.txt')
    env = 'local'
except FileNotFoundError:
    inputArr = sys.stdin.read().split('\n')
    inputI = 0
    f = None
    env = 'server'

def inputmethod():
    global inputI
    if f:
        return f.readline().strip()
    else:
        inputI+=1
        return inputArr[inputI-1]
        return input()



from collections import defaultdict as dd

n,m = [*map(int,inputmethod().split(' '))]

adj = dd(set)

for _ in range(m):
    a,b = [*map(int,inputmethod().split(' '))]
    adj[a-1].add(b-1)
    adj[b-1].add(a-1)

# 0: unseen
# 1: exploring
# 2: finished exploring
import sys
sys.setrecursionlimit(10**5+100)
def getNodeInCycle(adj, i, visited, parent):
    visited[i] = 1
    for near in adj[i]:
        if near==parent[i]:
            continue
        if near in visited:
            if visited[near]==1:
                parent[near] = i
                return near
            continue
        parent[near] = i
        result = getNodeInCycle(adj, near, visited, parent)
        if result:
            visited[i] = 2
            return result
    visited[i] = 2
    return None


visited = dict()
parent = [-1]*n
ans = []
for i in range(n):
    if i in visited:
        continue
    result = getNodeInCycle(adj,i,visited,parent)
    if not result:
        continue

    p = parent[result]
    ans.append(result)
    while(p!=result):
        ans.append(p)
        p = parent[p]

    ans.append(ans[0])
    print(len(ans))
    print(' '.join(map(str,map(lambda x:x+1,ans))))
    exit()

print("IMPOSSIBLE")