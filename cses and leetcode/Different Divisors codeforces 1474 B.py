import sys
inputI_23235231253 = -1
inputArr_6273468273 = []
try:
    open("__localsystemflag__").close()
    file_input_txt_2342349 = open('inp.txt')
    env = 'local'
except FileNotFoundError:
    rawInput_568279834 = sys.stdin.read()
    inputArr_6273468273 = rawInput_568279834.splitlines()
    
    inputI_23235231253 = 0
    file_input_txt_2342349 = None
    env = 'server'

def inputmethod():
    global inputI_23235231253
    if file_input_txt_2342349:
        return file_input_txt_2342349.readline().strip()
    else:
        inputI_23235231253+=1
        return inputArr_6273468273[inputI_23235231253-1]
        return input()


primes = [2]
p=3
while(p<20500):
    isPrime = True
    sqrtP = int(p**0.5)
    for px in primes:
        if px>sqrtP:
            break
        if p%px==0:
            isPrime = False
            break
    if isPrime:
        primes.append(p)
    p+=2
import bisect
t = int(inputmethod())
for _ in range(t):
    d = int(inputmethod())
    i = bisect.bisect_left(primes,1+d)
    j = bisect.bisect_left(primes,primes[i]+d)
    ans = primes[i]*primes[j]
    print(ans)