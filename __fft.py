
import math

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

    
def fft(p):
    if len(p)==1:
        return p


    n = len(p)
    assert n%2==0, "Length of input must be a power of 2"

    evens = p[::2]
    odds = p[1::2]

    evenFFT = fft(evens)
    oddFFT = fft(odds)

    w = pow(math.e,2*math.pi*1j/n)

    ans = [0]*n
    for i in range(n//2):
        ans[i] = evenFFT[i]+pow(w,i)*oddFFT[i]
        ans[i+n//2] = evenFFT[i]-pow(w,i)*oddFFT[i]

    return ans

def ifft(p):
    def inside(p):
        if len(p)==1:
            return p

        n = len(p)
        assert n%2==0, "Length of input must be a power of 2"

        evens = p[::2]
        odds = p[1::2]

        evenFFT = inside(evens)
        oddFFT = inside(odds)

        w = pow(math.e,-2*math.pi*1j/n)

        ans = [0]*n
        for i in range(n//2):
            ans[i] = evenFFT[i]+pow(w,i)*oddFFT[i]
            ans[i+n//2] = evenFFT[i]-pow(w,i)*oddFFT[i]

        return ans

    ans = inside(p)
    return [*map(lambda x:x/len(p),ans)]

