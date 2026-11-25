import math
import time


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

from collections import Counter
k,apples,bananas = [*map(int,inputmethod().split(' '))]
appleCounter = Counter(map(int,inputmethod().split(' ')))
bananaCounter = Counter(map(int,inputmethod().split(' ')))

applesArr = [0]*(k+1)
for key,v in appleCounter.items():
    applesArr[key]=v

bananaArr = [0]*(k+1)
for key,v in bananaCounter.items():
    bananaArr[key]=v

fftsize = 2**(math.ceil(math.log2(2*k)))

while(len(applesArr)<fftsize):
    applesArr.append(0)

while(len(bananaArr)<fftsize):
    bananaArr.append(0)

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


t = time.time()
appleFFT = fft(applesArr)
bananaFFT = fft(bananaArr)

pointWise = []
for i in range(len(appleFFT)):
    pointWise.append(appleFFT[i]*bananaFFT[i])

ans = ifft(pointWise)
ans = map(abs,ans)
ans = [*map(round,ans)]
ans = [*map(str,ans)]

finalAns = ans[2:2*k+1]
print(' '.join(finalAns))

print(time.time()-t)