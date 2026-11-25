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




n = int(inputmethod())
arr = [*map(int,inputmethod().split())]
arr.sort()

for i in range(n-1):
    arr[i+1]-=arr[i]
    arr[i] = 0

if arr[-1]==0:
    print("YES")
else:
    print("NO")