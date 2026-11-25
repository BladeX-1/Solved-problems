import math

import numpy as np

def myfft(poly):
    deg = len(poly)-1
    n = len(poly)

    assert n>=1

    twoPower = math.log2(n)
    assert int(twoPower)==twoPower,n

    if n==1:
        return [poly[0]]

    odds = poly[1::2]
    evens = poly[::2]

    assert len(odds)==n//2 and len(evens)==n//2,(odds,evens)

    fftOdds = myfft(odds)
    fftEvens = myfft(evens)

    assert len(fftOdds) == n//2 and len(fftEvens)==n//2, (len(fftOdds),print(fftEvens))

    ans = [0.0]*n

    w = pow(math.e,2*math.pi*1j/n)

    for i in range(0,n//2):# ?n
        ans[i] = fftEvens[i]+pow(w,i)*fftOdds[i]
        ans[i+n//2] = fftEvens[i]-pow(w,i)*fftOdds[i]


    return ans
def myifft(poly):
    def helper(poly):
        deg = len(poly)-1
        n = len(poly)

        assert n>=1

        twoPower = math.log2(n)
        assert int(twoPower)==twoPower,n

        if n==1:
            return [poly[0]]

        odds = poly[1::2]
        evens = poly[::2]

        assert len(odds)==n//2 and len(evens)==n//2,(odds,evens)

        fftOdds = helper(odds)
        fftEvens = helper(evens)

        assert len(fftOdds) == n//2 and len(fftEvens)==n//2, (len(fftOdds),print(fftEvens))

        ans = [0.0]*n

        w = pow(math.e,-2*math.pi*1j/n)

        for i in range(0,n//2):# ?n
            ans[i] = (fftEvens[i]+pow(w,i)*fftOdds[i])
            ans[i+n//2] = (fftEvens[i]-pow(w,i)*fftOdds[i])


        return ans

    ans = [*map(lambda x:x/len(poly),helper(poly))]
    return ans

arr = [23,5,21,23,5,32,3,5,23,2,5,23,5,235,2,35]
print(np.fft.fft(arr))
print(myfft(arr))
print(myifft(myfft(arr)))
print(np.fft.ifft(np.fft.fft(arr)))