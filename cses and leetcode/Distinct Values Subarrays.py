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


from collections import defaultdict as dd

n = int(inputmethod())
arr = [*map(int,inputmethod().split(' '))]

x2i = dict()
leftBoundry = -1

ans = 0
for i,x in enumerate(arr):
    if x in x2i and leftBoundry<x2i[x]:
        leftBoundry = x2i[x]
    temp=(i-leftBoundry)
    # print(temp)
    ans+=temp
    x2i[x] = i

print(ans)