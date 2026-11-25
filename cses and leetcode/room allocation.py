try:
    open("__localsystemflag__").close()
    f = open('inp.txt')
    env = 'local'
except FileNotFoundError:
    f = None
    env = 'server'

def inputmethod():
    if f:
        return f.readline().strip()
    else:
        return input()

n = int(inputmethod())
import heapq
import sys

heap = []
ans = 0
customers = []

for i in range(n):
    a,b = map(int,sys.stdin.readline().split(' '))
    assert a<=b
    customers.append((a,b,i))

customers.sort()
allocation = [-99]*n
emptyRooms = [*range(10)]
nextEmpty = 10

from collections import namedtuple

Customer = namedtuple("Customer",["exit","i"])

# heapq.heapify(emptyRooms)

for a,b,i in customers:
    while(heap and heap[0][0]<a):
        leavingCustomer = heapq.heappop(heap)
        heapq.heappush(emptyRooms,leavingCustomer[2])

    newRoom = heapq.heappop(emptyRooms)
    heapq.heappush(heap,(b,i,newRoom))
    if len(emptyRooms)==0:
        emptyRooms = [*range(nextEmpty,nextEmpty+10)]
        nextEmpty += 10
    allocation[i] = newRoom
    ans = max(ans,len(heap))

print(ans)
print(*map(lambda x:x+1,allocation))
