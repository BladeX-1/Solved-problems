import sys
inputI = -1
inputArr = []
try:
    open("__localsystemflag__").close()
    f = open('inp.txt')
    env = 'local'
except FileNotFoundError:
    inputArr = sys.stdin.read().split('\n')
    inputI = 0
    f = None
    env = 'server'

def inputmethod():
    global inputI
    if f:
        return f.readline().strip()
    else:
        inputI+=1
        return inputArr[inputI-1]
        return input()

def compute_xor_to_n(n):
    rem = n % 4
    if rem == 0: return n
    if rem == 1: return 1
    if rem == 2: return n + 1
    if rem == 3: return 0

    assert False

def compute_xor_l_to_r(l, r):
    return compute_xor_to_n(r) ^ compute_xor_to_n(l - 1)    

def xor_range_interesting(l,r,i,k):
    if i==0:
        return 0
    
    ans = compute_xor_l_to_r(l,r)

    low = ((l>>i)<<i)|k

    if low<l:
        low = (((l>>i)+1)<<i)|k
        assert low>=l
    
    high = ((r>>i)<<i)|k
    if high>r:
        high = (((r>>i)-1)<<i)|k
        assert high<=r


    if low>high:
        return ans

    ans^=(compute_xor_l_to_r(low>>i,high>>i)<<i)

    notInterestingCount = (high>>i)-(low>>i)+1
    if notInterestingCount%2==0:
        return ans
    else:
        return ans^k


t = int(inputmethod())
for _ in range(t):
    l,r,i,k = [*map(int,inputmethod().split(' '))]

    ans = xor_range_interesting(l,r,i,k)
    print(ans)