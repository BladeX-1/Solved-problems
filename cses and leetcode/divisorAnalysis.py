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
arr = []
for _ in range(n):
    x,power = [*map(int,inputmethod().split(' '))]
    arr.append((x,power))

M = 10**9+7

count = 1
for x,p in arr:
    count *= p+1
    count%=M

sum_ = 1
for x,p in arr:
    sum_ *= pow(x,p+1,M)-1
    sum_ %= M

    sum_ *= pow(x-1,-1,M)
    sum_ %= M


prodHelper = 1
for x,p in arr:
    prodHelper*=(p+1)
    prodHelper%=M-1

prod = 1
# twoInv = pow(2,-1,M-1)
for x,p in arr:
    if p%2==0:
        power = prodHelper*(p//2)
        power %= M-1

        prod *= pow(x,power,M)
        prod %= M

prodHelper = 1
dividedByTwo = False
for x,p in arr:
    if dividedByTwo or (p+1)%2!=0:
        prodHelper*=(p+1)
    else:
        prodHelper*=(p+1)//2
        dividedByTwo = True
    prodHelper%=M-1

for x,p in arr:
    if p%2==1:
        power = prodHelper*p
        power %= M-1

        prod *= pow(x,power,M)
        prod %= M

print(count,sum_,prod)