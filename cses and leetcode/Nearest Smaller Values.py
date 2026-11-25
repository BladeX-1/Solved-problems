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



n = int(inputmethod())
arr = [*map(int,inputmethod().split(' '))]

from collections import deque
space = deque()
ans = []
for i in range(n):
    while(space and arr[space[-1]]>=arr[i]):
        space.pop()
    if space:
        ans.append(space[-1])
    else:
        ans.append(-1)
    space.append(i)

print(*map(lambda x:x+1,ans))