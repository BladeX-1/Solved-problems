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



def query(n,k):
    if n<=1:
        return 1
    elif 1<n<k:
        return (query(n-1,k)+k)%n
    elif k<=n:
        g = query(n-n//k,k)
        if g<n%k:
            return (g-n)%(k+n)
        else:
            return k*(g-n%k)//(k-1)

    else:
        assert False

q = int(inputmethod())
n,k = [*map(int,inputmethod().split(' '))]
for _ in range(q):
    print(query(n,k))