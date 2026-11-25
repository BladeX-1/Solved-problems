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


n,k = [*map(int,inputmethod().split(' '))]
arr = [*map(int,inputmethod().split(' '))]

from itertools import combinations

ans = 0
sign = -1
for l in range(1,k+1):
    sign *= -1
    for comb in combinations(arr,l):
        prod = 1
        for c in comb:
            prod*=c
            if prod>n:
                break

        ans+=sign*(n//prod)

print(ans)