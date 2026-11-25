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


from collections import Counter

t = int(inputmethod())
for _ in range(t):
    n = int(inputmethod())
    s = inputmethod()

    left = [0]*n
    right = [0]*n

    leftCounter = Counter()
    rightCounter = Counter()

    for i in range(n):
        leftCounter[s[i]]+=1
        left[i] = len(leftCounter)

    for i in range(n):
        rightCounter[s[n-1-i]]+=1
        right[n-1-i] = len(rightCounter)

    ans = 0
    for i in range(n-1):
        ans = max(ans,left[i]+right[i+1])

    print(ans)