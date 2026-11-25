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

# now on, k>=2
arr = [*map(int,inputmethod().split(' '))]



import heapq
from collections import Counter

c = Counter(arr[:k-1])


heap = [[-1,x] for x in arr[:k-1]]
toRemove = set()

window = Counter(arr[:k-1])

ans = []
heapq.heapify(heap)
for i in range(k-1,n):
    if i!=0:
        toRemove.add(arr[i-k])
    window[arr[i]]+=1
    while(heap[0][1] in toRemove):
        top = heapq.heappop(heap)
        toRemove.remove(top[1])
        if top[0]-1>0:
            heapq.heappush(heap,[top[0]-1,top[1]])


    ans.append(heap[0][1])
    heapq.heappush(heap,[-1,arr[i]])

print(*ans)