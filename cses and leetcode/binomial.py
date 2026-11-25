M = 10**9+7

fact = [1,1]
for i in range(2,10**6+1):
    fact.append((fact[-1]*i)%M)

def C(n,r):
    return (fact[n]*pow(fact[r],-1,M)*pow(fact[n-r],-1,M))%M

# f = open('inp.txt','r')
def inputmethod():
    return input()
    return f.readline().strip()

n = int(inputmethod())
for _ in range(n):
    a,b = [*map(int,inputmethod().split(' '))]
    print(C(a,b))