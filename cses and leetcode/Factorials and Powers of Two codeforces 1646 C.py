import sys
inputI = -1
inputArr = []
spliter = "\n"
try:
    open("__localsystemflag__").close()
    f = open('inp.txt')
    env = 'local'
except FileNotFoundError:
    rawInput = sys.stdin.read()
    inputArr = rawInput.splitlines()
    
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

fact = [6]
for i in range(4,20):
    if fact[-1]*i>10**12:
        break
    fact.append(fact[-1]*i)

powerSetFact = set()

for mask in range(2**12):
    temp = 0
    for j in range(12):
        if (mask>>j)&1==1:
            temp+=fact[j]
    powerSetFact.add((temp,mask))

powerSetFact = list(powerSetFact)
powerSetFact.sort()

t = int(inputmethod())
for _ in range(t):
    n = int(inputmethod())
    ans = n.bit_count()
    for i in range(len(powerSetFact)):
        if powerSetFact[i][0]>n:
            break
        temp = (n-powerSetFact[i][0]).bit_count()+powerSetFact[i][1].bit_count()
        ans = min(temp,ans)
    print(ans)