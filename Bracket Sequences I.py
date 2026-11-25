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



n = int(inputmethod())
M = 10**9+7

def fact(x):
    ans = 1
    for i in range(2,x+1):
        ans*=i
        ans%=M
    return ans

def invFact(x):
    ans = 1
    for i in range(2,x+1):
        ans*=pow(i,-1,M)
        ans%=M
    return ans

def brac(m):
    if m%2==1:
        return 0
    else:
        m//=2
        ans = (fact(2*m)*invFact(m)**2*pow(m+1,-1,M))%M
        return ans

# open_ = 3
