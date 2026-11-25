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


from collections import defaultdict as dd
n = int(inputmethod())
arr = map(int,inputmethod().split())
arr2 = [*map(lambda x:x/abs(x),arr)]
assert len(arr2)==n, f"{n=} {len(arr2)=}"
cumuProd = 1
oldSigns = dd(int)
ansPositive = 0
ansNegative = 0
for i in range(n):
    cumuProd*=arr2[i]

    ansPositive+=oldSigns[1*cumuProd]+max(cumuProd,0)
    ansNegative+=oldSigns[-1*cumuProd]-min(cumuProd,0)


    
    oldSigns[cumuProd]+=1


print(int(ansNegative),int(ansPositive))