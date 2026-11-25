import sys
inputI_23235231253 = -1
inputArr_6273468273 = []
try:
    open("__localsystemflag__").close()
    file_input_txt_2342349 = open('inp.txt')
    env = 'local'
except FileNotFoundError:
    rawInput_568279834 = sys.stdin.read()
    inputArr_6273468273 = rawInput_568279834.splitlines()
    
    inputI_23235231253 = 0
    file_input_txt_2342349 = None
    env = 'server'

def inputmethod():
    global inputI_23235231253
    if file_input_txt_2342349:
        return file_input_txt_2342349.readline().strip()
    else:
        inputI_23235231253+=1
        return inputArr_6273468273[inputI_23235231253-1]
        return input()



n,k1,k2 = [*map(int,inputmethod().split())]
arr = [*map(int,inputmethod().split())]
brr = [*map(int,inputmethod().split())]

for i in range(n):
    if arr[i]>brr[i]:
        arr[i],brr[i] = brr[i],arr[i]

import heapq
heap = []
for i in range(n):
    heap.append([-(brr[i]-arr[i]),i])
heapq.heapify(heap)

a1 = k1
a2 = k2

while(a1):
    negDif,i = heapq.heappop(heap)
    if negDif==0:
        if a1%2==0:
    arr[i]+=1
    heapq.heappush(heap,[negDif+1,i])
    a1-=1

while(a2):
    negDif,i = heapq.heappop(heap)
    if negDif==0:
        if a2>=2:
            a2-=2
            continue
        else:
            brr[i]+=1
            continue

    brr[i]-=1
    heapq.heappush(heap,[negDif+1,i])
    a2-=1

sum_ = 0
for i in range(n):
    sum_ += (brr[i]-arr[i])**2

print(sum_)