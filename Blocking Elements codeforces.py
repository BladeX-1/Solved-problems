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



def tryFill(arr,m):
    n = len(arr)
    blocked = 0
    bucket = 0
    for i in range(arr):
        if bucket+arr[i]<=m:
            bucket+=arr[i]
        else:
            

t = int(inputmethod())
for _ in range(t):
    n = int(inputmethod())
    arr = [*map(int,inputmethod().split())]

    high = sum(arr)
    low = max(arr)

    ans = high

    while(low<=high):
        m = (low+high)//2

        filled = tryFill(arr,m)
        if filled:
            ans = m
            high = m-1
        else:
            low = m+1

    print(ans)
