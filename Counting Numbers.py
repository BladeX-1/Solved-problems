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




a,b = [*map(int,inputmethod().split(' '))]

import math

def f(n):
    digits = math.ceil(math.log10(n))
    ans = 0

    if digits-2>=0:
        ans+=10*9**(digits-2) ###### check for '0'

    s = str(n)
    i = digits-1
    for j,c in enumerate(s):
        if j==0:
            ans += (int(c)-1)*9**i
        else:
            ans += (int(c))*9**i
        
        i-=1

    # ans+=1
    return ans


print(f(b)-f(a))