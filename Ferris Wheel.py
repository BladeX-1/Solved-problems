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


n,x = [*map(int,inputmethod().split(' '))]
weights = [*map(int,inputmethod().split(' '))]

weights.sort()
import bisect

r = n-1
l=-1
count = 0
# print(n,weights)
while(len(weights)):
    l = bisect.bisect_left(weights,x-weights[r],0,r-1)

    if -1<l<=r and weights[l]>x-weights[r]:
        l-=1

    if l<=-1 or l>=r:
        count+=1
        del weights[r]
        r-=1
    else:
        count+=1
        del weights[r]
        del weights[l]
        r-=2

print(count)