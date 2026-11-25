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

s = ''
memo = set()
count = 0
import sys

sys.setrecursionlimit(10**6)
def fn(s):
    global memo,count

    if s in memo:
        return

    if len(s)==0:
        return
    
    memo.add(s)
    count+=1

    fn(s[1:])
    if len(s)>1 and s[0]!=s[1]:
        fn(s[0]+s[2:])
    

t = int(inputmethod())
for _ in range(t):
    n = int(inputmethod())
    s = inputmethod()

    count = 0
    memo.clear()
    fn(s)

    print(count)