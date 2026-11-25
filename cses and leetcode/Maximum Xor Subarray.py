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
arr = [*map(int,inputmethod().split(' '))]

cumu = [0]
for x in arr:
    cumu.append(cumu[-1]^x)

class Node:
    def __init__(self):
        self.val = -1
        self.zero = None
        self.one = None

preRoot = Node()
max_ = max(cumu)
import math
digits = math.floor(math.log2(max_))+1

# cumuStr = []
# for x in cumu:
#     temp = bin(x)[2:]
#     cumuStr.append('0'*(digits-len(temp))+temp)

# for x in cumuStr:
for x in cumu:
    r = preRoot
    for i in range(digits):
        # if x[i]=="0":
        if (x>>(digits-1-i))&1==0:
            if not r.zero:
                r.zero = Node()
            r = r.zero
        # elif x[i]=="1":
        if (x>>(digits-1-i))&1==1:
            if not r.one:
                r.one = Node()
            r = r.one
    r.val = x

a = preRoot
b = preRoot

def getBest(a,b,i):
    if i==digits:
        # anum = int(a.val,2)
        # bnum = int(b.val,2)
        # return anum^bnum
        return a.val^b.val
    
    ans = 0
    if a.one and b.zero:
        temp = getBest(a.one,b.zero,i+1)
        ans = max(ans,temp)
    if a.zero and b.one:
        temp = getBest(a.zero,b.one,i+1)
        ans = max(ans,temp)

    if not(a.one and b.zero) and not(a.zero and b.one):
        if a.one and b.one:
            temp = getBest(a.one,b.one,i+1)
        elif a.zero and b.zero:
            temp = getBest(a.zero,b.zero,i+1)
        else:
            assert False
        ans = max(ans,temp)

    return ans

def query(root,num,i):
    if i==digits:
        return int(root.val,2)
    
    if num[i]=='0' and root.one:
        return query(root.one,num,i+1)
    elif num[i]=='1' and root.zero:
        return query(root.zero,num,i+1)
    elif root.one:
        return query(root.one,num,i+1)
    else:
        return query(root.zero,num,i+1)

# ans = 0
# for i in range(n+1):
#     x = cumuStr[i]
#     temp = query(preRoot,x,0)^cumu[i]
#     ans = max(ans,temp)

# print(ans)
# exit()

if preRoot.one and preRoot.zero:
    ans = getBest(preRoot.one,preRoot.zero,1)
else:
    ans = getBest(preRoot,preRoot,0)
print(ans)
