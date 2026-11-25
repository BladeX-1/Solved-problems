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
    s = inputmethod()

    c = Counter(s)

    for i in range(len(s)):
        if s[i]=='1':
            if c["0"] == 0:
                break
            c["0"]-=1
        else:
            if c['1'] == 0:
                break
            c["1"]-=1

    print(c['1']+c['0'])