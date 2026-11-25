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


n,a,b = [*map(int,inputmethod().split(' '))]
arr = [*map(int,inputmethod().split(' '))]

cumu = [0]
for x in arr:
    cumu.append(cumu[-1]+x)

# arr[i]  -->  cumu[i+1]
# cumu[j]  --> arr[j-1]
# arr[0..x]  -->  cumu[1..x+1]

window = []
for i in range(a,b):# one is less on the upper limit
    while(window and window[-1]<cumu[i]):
        window.pop(-1)
    window.append(cumu[i])

# ans = window[0]-cumu[0]
ans = -float('inf')

for i in range(0,n-a+1):
    if i>0 and window[0] == cumu[i+a-1]:
        window.pop(0)
    if i+b<=n:
        while(window and window[-1]<cumu[i+b]):
            window.pop(-1)
        window.append(cumu[i+b])

    ans = max(ans,window[0]-cumu[i])

print(ans)