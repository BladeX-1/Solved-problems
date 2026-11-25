import math
import time


try:
    open("__localsystemflag__").close()
    f = open('inp.txt')
    env = 'local'
except FileNotFoundError:
    f = None
    env = 'server'

def inputmethod():
    if f:
        return f.readline().strip()
    else:
        return input()



n, windowSize = [*map(int,inputmethod().split(' '))]
x,a,b,c = [*map(int,inputmethod().split(' '))]
arr = [0]*(n)

for i in range(n):
    arr[i] = x
    x = (a*x+b)%c

partitionSize = windowSize
orPre = []
for i in range(n):
    if i%partitionSize == 0:
        orPre.append([arr[i]])

    else:
        orPre[-1].append(orPre[-1][-1] | arr[i])

orSuf = []
for i in reversed(range(n)):
    if i%partitionSize == partitionSize-1 or i==n-1:
        orSuf.append([arr[i]])
    else:
        orSuf[-1].append(orSuf[-1][-1] | arr[i])

orSuf.reverse()
for i in range(len(orSuf)):
    orSuf[i].reverse()

# print(*map(bin,arr))
# print(*map((lambda x:list(map(bin,x))),orPre))
# print(*map((lambda x:list(map(bin,x))),orSuf))
# exit()

ans = []
for i in range(n-windowSize+1):
    suf = orSuf[i//partitionSize][i%partitionSize]
    pre = orPre[(i+windowSize-1)//partitionSize][(i+windowSize-1)%partitionSize]
    ans.append(suf | pre)

xors = 0
for i in range(len(ans)):
    xors^=ans[i]

print(xors)