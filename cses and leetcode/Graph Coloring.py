'''
for each node i from 0 to n-1
    try a color
    and then enter checking i+1 node

avoid skiping the colors
    like 0 1 3, without any '2' in the graph
preput color for 0 as 0
exit immediately if answer is getting >= alreadyBestAns
start ans as outEdges+1
only iterate colors till maxAns
    
'''

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
n, edges = [*map(int,inputmethod().split(' '))]
adjx = [set() for _ in range(n)]
for _ in range(edges):
    a,b = [*map(int,inputmethod().split(' '))]
    assert a!=b
    adjx[a-1].add(b-1)
    adjx[b-1].add(a-1)


adj = [[] for _ in range(n)]
fullyConnected = 0
noConnected = 0
maxEdges = 0
for i in range(n):
    adj[i] = list(adjx[i])
    maxEdges = max(maxEdges,len(adj[i]))
    if len(adj[i])==n-1:
        fullyConnected+=1

if fullyConnected==n:
    print(n)
    print(*range(1,n+1))
    exit()
elif maxEdges==0:
    print(1)
    print(*([1]*n))
    exit()

def bt(adj,i,n,colors,counterColors,bestAns,colorsAns,maxColor):
    if i==n:
        bestAns[0] = len(counterColors)
        colorsAns.append(colors[:])
        return True
    
    for c in range(bestAns[0]):
        works = True
        for near in adj[i]:
            if colors[near] == c:
                works = False
                break
        if not works:
            continue
        
        colors[i] = c
        counterColors[c]+=1
        shouldBreak = False
        if len(counterColors)>bestAns[0]:
            shouldBreak = True
        if maxColor+1<c:
            shouldBreak = True
        if not shouldBreak:
            if len(counterColors)==bestAns[0] and len(colorsAns)>0:
                isSolved = False
            else:
                shouldBreak = False
                isSolved = bt(adj,i+1,n,colors,counterColors,bestAns,colorsAns,max(maxColor,c))
        else:
            isSolved = False
        # no need to try different color for the last node if answer is already found with one color
        counterColors[c]-=1
        colors[i] = -1
        if counterColors[c]==0:
            del counterColors[c]
        if isSolved and i==n-1:
            return True

        if shouldBreak:
            break
        
    return False


from collections import Counter

colors = [-1]*n
colors[0] = 0
colorsAns = []
ans = [maxEdges+1]
counterColors = Counter()
counterColors[0] += 1
bt(adj,1,n,colors,counterColors,ans,colorsAns,0)
print(ans[0])
for i in range(len(colorsAns)):
    colors = colorsAns[i]
    counter = Counter(colors)
    if len(counter)==ans[0]:
        print(*map(lambda x:x+1,colors))
        break