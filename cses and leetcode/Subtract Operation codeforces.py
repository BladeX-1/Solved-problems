import sys
inputI = -1
inputArr = []
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

    arrSet = set(arr)
    exists = False
    for x in arrSet:
        if x+k in arrSet:
            exists = True
            break

    if exists:
        print("YES")
    else:
        print("NO")