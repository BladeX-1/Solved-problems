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



t = int(inputmethod())
for _ in range(t):
    n,k,b,s = [*map(int,inputmethod().split(' '))]

    s-=k*b

    if s<0 or s>(k-1)*n:
        print(-1)
        continue

    arr = [0]*n
    # distribute for the 'b'
    for i in range(n):
        arr[i]+=k*(b//n) # distribute equally among the 'n'
        if i<b%n: # add additional k for the remainders
            arr[i]+=k

    for i in range(n):
        if s>=k-1:
            arr[i]+=k-1
            s-=k-1
        else:
            arr[i]+=s
            break

    ans = ' '.join(map(str,arr))
    print(ans)