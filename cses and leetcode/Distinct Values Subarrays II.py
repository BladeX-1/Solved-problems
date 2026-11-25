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



n,k = [*map(int,inputmethod().split(' '))]
arr = [*map(int,inputmethod().split(' '))]

from collections import Counter
class MyCounter:
    def __init__(self):
        self.counter = Counter()
    def add(self,x):
        self.counter[x]+=1
    def remove(self,x):
        self.counter[x]-=1
        if self.counter[x]==0:
            del self.counter[x]
    def __len__(self):
        return len(self.counter)


ans = 0
c = MyCounter()
l=0
for r in range(n):
    c.add(arr[r])
    while(len(c)>k):
        c.remove(arr[l])
        l+=1
    ans += r-l+1
print(ans)