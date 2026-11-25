from collections import Counter
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



s = [*map(int,inputmethod())]
originalLength = len(s)
maxLen = 2*len(s)-1
maxLen = 2**math.ceil(math.log2(maxLen))

srev = s[::-1]

for i in range(len(s),maxLen):
    s.append(0)
    srev.append(0)

ffts = fft(s)
fftsrev = fft(srev)

result = [a*b for a,b in zip(ffts,fftsrev)]
result = ifft(result)
result = [round(abs(x)) for x in result]

s = ' '.join(map(str, result[originalLength:2*originalLength-1]))
print(s)

# import numpy as np
# print(*np.convolve(s, s[::-1]))