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




s = inputmethod()
k = int(inputmethod())
n = len(s)
from collections import defaultdict as dd

class Node:
    def __init__(self):
        self.children = dd(Node)
        self.word: None|str = None

root = Node()
for _ in range(k):
    word = inputmethod()
    if len(word)>n:
        continue

    r = root
    for c in word:
        r = r.children[c]

    r.word = word


counts = [0]*n
M = 10**9+7
def getCount(mainRoot,s,i,memo):
    if i==n:
        return 1 ################### check, can also be '0'

    if i in memo:
        return memo[i]
    
    r = mainRoot
    ans = 0
    for j in range(i,n):
        if s[j] in r.children:
            r = r.children[s[j]]
        else:
            break

        if r.word:
            ans += getCount(mainRoot,s,j+1,memo)

    ans%=M
    memo[i] = ans
    return ans

# import time
# t = time.time()
memo = dict()
for i in reversed(range(n)):
    getCount(root,s,i,memo)
ans = getCount(root,s,0,memo)
print(ans)
# print(time.time()-t)