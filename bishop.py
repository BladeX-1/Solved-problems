f = open('inp.txt','r')

def inputmethod():
    return f.readline().strip()


M = 10**9+7
fact = [1,1]
for i in range(2,500+1):
    fact.append((fact[-1]*i)%M)

def C(n,r):
    if r>n:
        return 0
    return (fact[n]*(pow(fact[r],-1,M)*pow(fact[n-r],-1,M)))%M

def bishop(n,k):
    ans = 0
    for w in range(0,min(k+1,n+1)):
        b = k-w

        if n%2==0:
            ans += (C(n,w)*C(n-1,w)*C(n,b)*C(n-1,b))%M
        else:
            ans += (C(n,w)*C(n,w)*C(n-1,b)*C(n-1,b))%M
        ans%=M

    return ans


n,k = [*map(int,inputmethod().split(' '))]

for n,k in [(1,0),(1,1),(1,3),(2,0),(2,1),(2,2),(2,3),(2,4),(2,5),(3,0),(3,1),(5,4)]:
    ans = bishop(n,k)
    print((n,k),ans)