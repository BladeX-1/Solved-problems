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

from itertools import permutations

fact = [1] * 21
for i in range(1,21):
    fact[i] = fact[i-1] * i

def p(n,k):
    k-=1
    numbers = [i for i in range(1,n+1)]
    ans = []

    while(numbers):
        i = k//fact[(len(numbers)-1)]
        ans.append(numbers[i])
        k -= i*fact[len(numbers)-1]
        del numbers[i]

    return ans

def invP(n,p):
    numbers = [i for i in range(1,n+1)]
    ans = 0
    for j in range(n):
        i = numbers.index(p[j])
        ans+=fact[len(numbers)-1]*i
        del numbers[i]

    return ans+1

# for i in range(1,20):
#     perm = p(5,i)
#     inv = invP(5,perm)
#     print(5,i,perm,inv)


t = int(inputmethod())

for _ in range(t):
    code,n,*data = [*map(int,inputmethod().split(' '))]
    if code==1:
        k = data[0]
        perm = p(n,k)
        print(*perm)
    if code==2:
        perm = data
        print(invP(n,perm))
