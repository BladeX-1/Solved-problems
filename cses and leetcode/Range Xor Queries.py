try:
    open("__localsystemflag__").close()
    f = open('inp.txt')
    env = 'local'
except FileNotFoundError:
    f = None
    env = 'server'
import sys
def inputmethod():
    if f:
        return f.readline().strip()
    else:
        return sys.stdin.readline()
        return input()



n, q = [*map(int,inputmethod().split(' '))]
arr = [*map(int,inputmethod().split(' '))]

cumu = [0]
for x in arr:
    cumu.append(cumu[-1]^x)

# cumu[i] = XOR till arr[i-1]
# arr[i] map to cumu[i+1]
ans = []
for _ in range(q):
    a,b = [*map(int,inputmethod().split(' '))]
    ans.append(str(cumu[b]^cumu[a-1]))

print(' '.join(ans))