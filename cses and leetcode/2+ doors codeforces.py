import sys
inputI = -1
inputArr = []
spliter = "\n"
try:
    open("__localsystemflag__").close()
    f = open('inp.txt')
    env = 'local'
except FileNotFoundError:
    rawInput = sys.stdin.read()
    inputArr = rawInput.splitlines()
    
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

n,q = [*map(int,inputmethod().split())]
adj = [dict() for _ in range(n)]
ans = [2**30-1]*n
fixed = set()
for _ in range(q):
    i,j,x = [*map(int,inputmethod().split())]
    i,j = min(i,j),max(i,j)
    i-=1
    j-=1

    if i==j:
        ans[i] = x
        fixed.add(i)
    else:
        adj[i][j] = x
        adj[j][i] = x

for i in range(n):
    for j in adj[i]:
        x = adj[i][j]

        # set the zeros
        ans[i]&=x
        ans[j]&=x


for i in range(n):
    if i in fixed:
        continue
    nearAnd = 2**30-1
    for j in adj[i]:
        nearAnd &= ans[j]

    ans[i]&=(~nearAnd)

print(*ans)