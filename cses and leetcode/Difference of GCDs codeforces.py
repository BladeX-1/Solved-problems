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
    n,l,r = [*map(int,inputmethod().split())]

    solutionExists = True
    solution = []
    for i in range(1,n+1):
        if r//i == (l-1)//i:
            solutionExists = False
            break

        solution.append((l-1+i-(l-1)%i))

    if not solutionExists:
        print("NO")
    else:
        print("YES")
        print(*solution)