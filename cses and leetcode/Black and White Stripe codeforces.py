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
    arr = [*map(lambda c:int(c=='B'),inputmethod())]
    # white == 0, black == 1

    blacksInWindow = sum(arr[:k])
    ans = blacksInWindow
    for i in range(k,n):
        blacksInWindow+=arr[i]-arr[i-k]
        ans = max(ans,blacksInWindow)

    print(k-ans)