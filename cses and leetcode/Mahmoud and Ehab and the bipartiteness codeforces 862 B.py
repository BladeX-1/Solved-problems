import sys
inputI_23235231253 = -1
inputArr_6273468273 = []
try:
    open("__localsystemflag__").close()
    file_input_txt_2342349 = open('inp.txt')
    env = 'local'
except FileNotFoundError:
    rawInput_568279834 = sys.stdin.read()
    inputArr_6273468273 = rawInput_568279834.splitlines()
    
    inputI_23235231253 = 0
    file_input_txt_2342349 = None
    env = 'server'

def inputmethod():
    global inputI_23235231253
    if file_input_txt_2342349:
        return file_input_txt_2342349.readline().strip()
    else:
        inputI_23235231253+=1
        return inputArr_6273468273[inputI_23235231253-1]
        return input()


n = int(inputmethod())
from collections import defaultdict as dd
adj = [set() for _ in range(n)]

for _ in range(n-1):
    a,b = [*map(int,inputmethod().split())]
    adj[a-1].add(b-1)
    adj[b-1].add(a-1)


colors = [-1]*n

def fillColors(adj,j,c):
    # for near in adj[j]:
    #     if colors[near]==c:
    #         return False
    colors[j] = c
    nexts = []
    for near in adj[j]:
        if colors[near]==-1:
            nexts.append(near)
            # fillColors(adj,near,c^1)
    return nexts

nexts = [0]
cl = 0
nexts2 = []
while(nexts2 or nexts):
    for i in nexts:
        temp = fillColors(adj,i,cl)
        nexts2.extend(temp)

    nexts = nexts2
    nexts2 = []
    cl ^= 1
    

# assert temp==True
assert -1 not in colors

from collections import Counter
c = Counter(colors)

ans = c[0]*c[1]-(n-1)
print(ans)