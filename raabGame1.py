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
    
t = int(inputmethod())

for _ in range(t):
    n,a,b = [*map(int,inputmethod().split(' '))]

    if a+b>n:
        print('NO')
        continue

    draws = n-a-b

    if a==0 and b==0:
        print('YES')
        print(*range(1,n+1))
        print(*range(1,n+1))
        continue

    if a==0 or b==0:
        print('NO')
        continue

    print('YES')
    arr = [*range(n,n-draws,-1)]
    brr = [*range(n,n-draws,-1)]

    n = a+b

    arr.extend(range(1,n+1))

    zrr = list(range(1,n+1))

    # shift by 'b'
    brr.extend(zrr[b:]+zrr[:b])

    print(*arr)
    print(*brr)