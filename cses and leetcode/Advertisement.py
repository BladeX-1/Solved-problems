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



def largestRectangleArea(heights):
    leftSmall = nextSmallestLeft(heights)
    rightSmall = nextSmallestRight(heights)
    n = len(heights)
    bestAns = 0
    for i in range(n):
        
        left = leftSmall[i]+1
        right = rightSmall[i]-1 if rightSmall[i]!=-1 else n-1
        bestAns = max(bestAns, heights[i]*(right-left+1))
    return bestAns

def max(a,b):
    return a if a>=b else b

from collections import deque

def nextSmallestLeft(arr):
    stk = deque()
    ans = []
    for i,x in enumerate(arr):
        while(len(stk)>0 and stk[-1][1]>=x):# need to check if it is > or >=
            stk.pop()
        if(len(stk)==0):
            ans.append(-1)
        else:
            ans.append(stk[-1][0])
        stk.append((i,x))
    return ans

def nextSmallestRight(arr):
    stk = deque()
    revAns = deque()
    for i in reversed(range(len(arr))):
        x = arr[i]
        while(len(stk)>0 and stk[-1][1]>=x):# need to check if it is > or >=
            stk.pop()
        if(len(stk)==0):
            revAns.appendleft(-1)
        else:
            revAns.appendleft(stk[-1][0])
        stk.append((i,x))
    return revAns


n = int(inputmethod())
arr = [*map(int,inputmethod().split(' '))]

ans = largestRectangleArea(arr)
print(ans)