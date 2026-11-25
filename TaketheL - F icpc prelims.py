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



t = int(input())
for _ in range(t):
    n = int(input())
    xyArr = []
    for _ in range(n):
        xy = [*map(int,input().split())]
        xyArr.append(xy)

    xyArr.sort()

    ys = []
    for x,y in xyArr:
        ys.append(y)

    # A |__
    #
    # B  __
    #      |

    if n<=2:
        print("YES")
        continue
    

    inf=float('inf')
    ARange = [-inf,inf]
    BRange = [-inf,inf]

    # start with A
    BRange[0] = ys[0]
    ARange[1] = ys[1]

    for i in range(1,n):
        if BRange[0]<ys[i]:
            2