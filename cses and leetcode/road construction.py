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


n,m = [*map(int,inputmethod().split(' '))]
edges = []
for _ in range(m):
    a,b = [*map(int,inputmethod().split(' '))]
    edges.append([a,b])

componentsCount = n
maxComponentSize = 1

dsu = [*range(n)]
dsuSize = [1]*n
def add(a,b):
    global maxComponentSize,componentsCount

    aes = []
    p = a
    while(dsu[p]!=p):
        aes.append(p)
        p = dsu[p]
    aes.append(p)

    bes = []
    p = b
    while(dsu[p]!=p):
        bes.append(p)
        p = dsu[p]
    bes.append(p)



    assert dsu[aes[-1]]!=dsu[bes[-1]]

    size1 = dsuSize[aes[-1]]
    size2 = dsuSize[bes[-1]]

    maxComponentSize = max(maxComponentSize,size1+size2)
    componentsCount-=1
    
    if len(aes)>len(bes):
        for i in aes:
            dsu[i] = dsu[bes[-1]]
        dsuSize[bes[-1]] = size1+size2
    else:
        for i in bes:
            dsu[i] = dsu[aes[-1]]
        dsuSize[aes[-1]] = size1+size2
    
def find(x):
    p = x
    while(p!=dsu[p]):
        p = dsu[p]
    return p


for i in range(len(edges)):
    a,b = edges[i]
    try:
        add(a-1,b-1)
    except AssertionError:
        pass
    print(componentsCount,maxComponentSize)