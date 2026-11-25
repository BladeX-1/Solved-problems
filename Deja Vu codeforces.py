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



t = int(inputmethod())
for _ in range(t):
    n,q = [*map(int,inputmethod().split(' '))]
    arr = [*map(int,inputmethod().split(' '))]
    xrr = [*map(int,inputmethod().split(' '))]

    for x in xrr:
        for i in range(n):
            rightMostSet = arr[i]&(-arr[i])
            twoPowerXi = 1<<(x)

            if rightMostSet>=twoPowerXi:
                arr[i]+=twoPowerXi>>1

    arrMap = map(str,arr)
    print(' '.join(arrMap))
