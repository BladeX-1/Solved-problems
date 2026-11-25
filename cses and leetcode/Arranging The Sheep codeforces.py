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
    n = int(inputmethod())
    s = inputmethod()
    sheeps = []
    for i in range(n):
        if s[i]=='*':
            sheeps.append(i-len(sheeps))

    sheeps.sort()
    if len(sheeps)==0:
        print(0)
        continue

    m = sheeps[len(sheeps)//2]

    ans = 0
    for s in sheeps:
        ans+=abs(m-s)

    print(ans)
    