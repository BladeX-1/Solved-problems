
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

    assert len(p)%2 == 0, "Length of input must be a power of 2"

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


lenSig,lenMask = [*map(int,inputmethod().split(' '))]
sig = [*map(int,inputmethod().split(' '))]
mask = [*map(int,inputmethod().split(' '))]

maxLen = len(sig)+len(mask)-1
maxLen = 2**math.ceil(math.log2(maxLen))

mask.reverse()
sig+=[0]*(maxLen-len(sig))
mask+=[0]*(maxLen-len(mask))

# import numpy as np
# con = np.convolve(sig,mask)
# print(con)

sigFFT = fft(sig)
maskFFT = fft(mask)
resultFFT = [a*b for a, b in zip(sigFFT, maskFFT)]
result = ifft(resultFFT)
result = [round(abs(x)) for x in result]
result = result[:lenSig+lenMask-1]
print(*result)