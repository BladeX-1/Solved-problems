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
    s = [1]+[*map(int,list(inputmethod()))]

    cost = 0
    added = set()
    for i in range(1,n+1):
        for j in range(i,n+1,i):
            if s[j]==1:
                break

            if j in added:
                continue
            added.add(j)
            cost += i

    print(cost)