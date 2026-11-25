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



n,m = [*map(int,inputmethod().split(' '))]

fact = [0]*(2*10**6+1)
fact[0]=1
M = 10**9+7
for i in range(1,2*10**6+1):
    fact[i] = (fact[i-1]*i)%M

def c(n,r):
    return (fact[n]*pow(fact[n-r],-1,M)*pow(fact[r],-1,M))%M

print(c(n+m-1,m))