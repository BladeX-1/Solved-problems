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


n, target = [*map(int,inputmethod().split(' '))]
arr = [*map(int,inputmethod().split(' '))]

from collections import defaultdict as dd
sumsLeft = dd(int)
sumsRight = dd(int)

sumsLeft[0]+=1
sumsRight[0]+=1

for i in range(n//2):
    for sumValue,count in sumsLeft.copy().items():
        sumsLeft[sumValue+arr[i]]+=count
    
for i in range(n//2,n):
    for sumValue,count in sumsRight.copy().items():
        sumsRight[sumValue+arr[i]]+=count


ans = 0
for sumValue,count in sumsLeft.items():
    if target-sumValue in sumsRight:
        ans+=count*sumsRight[target-sumValue]

print(ans)