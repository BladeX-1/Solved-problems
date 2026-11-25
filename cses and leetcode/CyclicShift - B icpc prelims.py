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
    arr = [*map(int,inputmethod().split(' '))]

    if n==1:
        print(0)
        continue
    elif n==2:
        print(abs(arr[0]-arr[1]))
        continue

    assert n>=3, "something wrong with input"

    a = abs(arr[0]-arr[-1])
    b = abs(arr[1]-arr[0])

    first = max(a,b)
    second = min(a,b)

    for r in range(2,n):
        temp = abs(arr[r]-arr[r-1])
        if temp>=first:
            second = first
            first = temp
        elif temp>=second:
            second = temp

    print(second)