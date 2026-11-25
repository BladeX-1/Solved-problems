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
    n = int(inputmethod())
    arr = [*map(int,inputmethod().split(' '))]

    intervals = []
    start = None
    for i in range(n):
        if i==0 or abs(arr[i-1])%2==abs(arr[i])%2:
            start = i

        if i==n-1 or abs(arr[i])%2==abs(arr[i+1])%2:
            end = i
            intervals.append([start,end])

    ans = -float('inf')
    for start,end in intervals:
        cumu = [0]
        for i in range(start,end+1):
            cumu.append(cumu[-1]+arr[i])

        left = float('inf')
        for i in range(len(cumu)):
            if cumu[i]-left>ans:
                ans = cumu[i]-left
            if cumu[i]<left:
                left = cumu[i]

    print(ans)