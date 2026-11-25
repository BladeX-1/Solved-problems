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
adj = dd(list)
for _ in range(m):
    a,b = [*map(int,inputmethod().split(' '))]
    adj[a-1].append(b-1)


sys.setrecursionlimit(10**5+100)
def fillTopo(adj, i, visited, revTopo):
    for near in adj[i]:
        if near in visited:
            continue
        visited.add(near)
        fillTopo(adj, near, visited, revTopo)
    revTopo.append(i)

M = 10**9+7
def graph_dfs(adj, i):
    if dp[i]!=-1:
        return dp[i]
    
    ans = 0
    for near in adj[i]:
        ans += graph_dfs(adj, near)

    ans%=M
    dp[i] = ans
    return ans

revTopo = []
visited = set()
for i in range(n):
    fillTopo(adj,i,visited,revTopo)

dp = [-1]*n
dp[n-1] = 1

for i in revTopo:
    graph_dfs(adj,i)
ans = graph_dfs(adj,0)
print(ans)