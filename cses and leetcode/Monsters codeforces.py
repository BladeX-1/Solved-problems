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


import heapq

t = int(inputmethod())
for _ in range(t):
    n,k = [*map(int,inputmethod().split(' '))]
    healths = [*map(lambda x:x%k if x%k!=0 else k,map(int,inputmethod().split(' ')))]

    healths2 = [[]]*n
    for i in range(n):
        healths2[i] = [-healths[i],i+1]

    healths2.sort()

    ansMap = map(lambda x:x[1],healths2)
    print(' '.join(map(str,ansMap)))