try:
    open("__localsystemflag__").close()
    f = open('inp.txt')
    env = 'local'
except FileNotFoundError:
    f = None
    env = 'server'

import sys
def inputmethod():
    if f:
        return f.readline().strip()
    else:
        return sys.stdin.readline()
        return input()





n = int(inputmethod())
intervals = []
for _ in range(n):
    a,b = [*map(int,inputmethod().split(' '))]
    intervals.append((a,1))
    intervals.append((b,-1))

intervals.sort()
currentInside = 0
maxCustomers = 0
for a,x in intervals:
    currentInside+=x
    maxCustomers = max(currentInside,maxCustomers)

print(maxCustomers)

exit()
import heapq
heap = []
ans = 0
for a,b in intervals:
    while(heap and heap[0]<=a):## ??????????? should i put equal here?
        heapq.heappop(heap)
    heapq.heappush(heap,b)
    ans = max(ans,len(heap))

print(ans)