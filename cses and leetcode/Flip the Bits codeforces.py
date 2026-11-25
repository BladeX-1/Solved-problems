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
for _t in range(t):
    if _t == 2:
        pass
    n = int(inputmethod())
    a = [*map(int,list(inputmethod()))]
    b = [*map(int,list(inputmethod()))]

    zeroOne = [0,0]
    ends = [-1]
    for i in range(n):
        zeroOne[a[i]]+=1
        if zeroOne[0]==zeroOne[1]:
            ends.append(i)


    if a[ends[-1]+1:n]!=b[ends[-1]+1:n]:
        print("NO")
        continue

    r = ends[-1]
    solutionExists = True
    for e in reversed(ends):
        if e==n-1 or r==e:
            continue
        aBin = int(''.join(map(str,a[e+1:r+1])),base=2)
        bBin = int(''.join(map(str,b[e+1:r+1])),base=2)

        bitLen = r-e
        r = e

        # already equal OR  can be made equal
        if not((aBin==bBin) or (aBin^bBin)+1==2**bitLen):
            solutionExists = False
            break

    if solutionExists:
        print("YES")
    else:
        print("NO")