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
    n,k = [*map(int,inputmethod().split(' '))]
    arr = [*map(int,inputmethod().split(' '))]

    arr.sort()
    finalLengthLHigh = n-k

    windowSum = 0
    for i in range(finalLengthLHigh):
        windowSum+=arr[i]

    ans = windowSum
    l = 0
    for i in range(finalLengthLHigh,n):
        windowSum+=arr[i]-arr[l]-arr[l+1]
        l+=2
        ans = max(ans,windowSum)

    print(ans)