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

    
primes = [2]
for p in range(3, 10**3+1, 2):
    isPrime = True
    for prime in primes:
        if prime*prime>p:
            break
        if p%prime==0:
            isPrime = False
            break
    if isPrime:
        primes.append(p)

factors = [None]*(10**6+1)
for i in range()