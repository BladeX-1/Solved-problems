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



n = int(inputmethod())
arr = [*map(int,inputmethod().split(' '))]

x2i = dict()

sameOnLeftAt = []
for i in range(n):
    if arr[i] in x2i:
        sameOnLeftAt.append(x2i[arr[i]])
    else:
        sameOnLeftAt.append(-1)

    x2i[arr[i]] = i

x2i.clear()
sameOnRightAt = []
for i in reversed(range(n)):
    if arr[i] in x2i:
        sameOnRightAt.append(x2i[arr[i]])
    else:
        sameOnRightAt.append(n)

    x2i[arr[i]] = i
sameOnRightAt.reverse()

ans = 0
for i in range(n):
    lefti = sameOnLeftAt[i]
    righti = sameOnRightAt[i]

    ans+=(i-lefti)*(righti-i)

print(ans)