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



n = int(inputmethod())
adj = [[] for _ in range(n)]
totalEdges = n-1
for _ in range(n-1):
    a,b = [*map(int,inputmethod().split(' '))]
    a-=1
    b-=1
    adj[a].append(b)
    adj[b].append(a)

color = [-1]*n
for i in range(n):
    for c in range(2):
        color[i] = c
        failed = False
        for near in adj[i]:
            if color[near] == c:
                failed = True
                break
        if failed:
            continue
        else:
            break

assert -1 not in color
# print(color)
ans = max(color.count(0),color.count(1))
print(ans)