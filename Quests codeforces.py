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



t = int(input())
import heapq
for _ in range(t):
    n,k = [*map(int,input().split(' '))]
    arr = [*map(int,input().split(' '))]
    brr = [*map(int,input().split(' '))]

    availables = [[arr[0],0,0]]
    ans = 0
    for i in range(k):
        ansTemp,iTemp,cTemp = availables[0]
        ans+=ansTemp

        if cTemp==0:
            heapq.heappop(availables)
            if iTemp+1<n:
                heapq.heappush(availables,[arr[iTemp+1],iTemp+1,0])
            heapq.heappush(availables,[brr[iTemp],iTemp,1])