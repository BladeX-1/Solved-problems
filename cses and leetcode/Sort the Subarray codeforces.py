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
    arr1 = [*map(int,inputmethod().split())]
    arr2 = [*map(int,inputmethod().split())]

    difArr = []
    for i in range(n):
        if arr1[i]!=arr2[i]:
            difArr.append(1)
        else:
            difArr.append(0)

    difArrCumu = [0]
    for i in range(n):
        difArrCumu.append(difArrCumu[-1]+difArr[i])

    # del difArr

    sortedIntervals = []
    l = r = -1
    for i in range(n):
        if i==0 or arr2[i-1]>arr2[i]:
            l = i

        if i==n-1 or arr2[i]>arr2[i+1]:
            r = i
            sortedIntervals.append([l,r])

    bestLen = 0
    bestL = 0
    bestR = -1

    for l,r in sortedIntervals:
        if r-l+1>bestLen and difArrCumu[r+1]!=difArrCumu[l]:
            bestL = l+1
            bestR = r+1
            bestLen = r-l+1

    print(bestL,bestR)