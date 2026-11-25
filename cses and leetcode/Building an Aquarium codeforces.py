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
    n,x = [*map(int,inputmethod().split(' '))]
    arr = [*map(int,inputmethod().split(' '))]

    low = min(arr)
    high = (x//n)+max(arr)
    ans = 1
    while(low<=high):
        mid = (low+high)//2

        # try filling
        filled = 0
        for i in range(n):
            filled+=max(0,mid-arr[i])

        if filled>x:
            high = mid-1
        else:
            ans = mid
            low = mid+1

    print(ans)