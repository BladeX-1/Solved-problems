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


from collections import Counter
t = int(inputmethod())
for _ in range(t):
    n,k = [*map(int,inputmethod().split())]
    arrMap = map(int,inputmethod().split())
    arrModMap = map(lambda x:x%k,arrMap)

    arrCounter = Counter(arrModMap)

    maxVals = []
    maxCount = -1

    for val,freq in arrCounter.items():
        if val==0:
            continue
        if freq>maxCount:
            maxVals = [val]
            maxCount = freq
        elif freq==maxCount:
            maxVals.append(val)

    if len(maxVals)==0:
        print(0)
        continue
    temp = min(maxVals)
    ans = k*(maxCount-1)+(k-temp+1)
    print(ans)