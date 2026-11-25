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
    


n = int(inputmethod())
arr = [*map(lambda x:x-1,map(int,inputmethod().split(' ')))]
powers = dict()
power = 1
powers[power] = arr[:]
def operate(arr1,arr2):
    assert len(arr1)==len(arr2)
    arr = [-1]*len(arr1)
    for i in range(len(arr1)):
        arr[i] = arr2[arr1[i]]
    return arr

for i in range(2,2**math.ceil(math.log2(2*10**5))+1):
    powers[i] = operate(powers[i-1],powers[i-1])

divisors = []
for i in range(1,n+1):
    if n%i==0:
        divisors.append(i)

def getPower(d):
    if d==1:
        return powers[1]
    
    half = getPower(d//2)
    ans = operate(half,half)
    if d%2==1:
        ans = operate(ans,powers[1])

    return ans

I = [*range(n)]
for d in divisors:
    power = getPower(d)
    if I==power:
        c(d)
        break
