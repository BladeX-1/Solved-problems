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



t = int(inputmethod())
for _ in range(t):
    n,k = [*map(int,inputmethod().split())]
    arr = [*map(int,inputmethod().split())]


    # tempArr = [0]*n
    # mul = 1
    # for i in range(n):
    #     tempArr[i] = arr[i]*mul
    #     mul*=2

    ans = 0
    l = 0
    for r in range(n):
        if r==n-1 or arr[r]>=(arr[r+1]<<1):
            ans+=max(0,r-l+1-k)
            l = r+1

    print(ans)