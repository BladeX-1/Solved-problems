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


def binaryRight(arr,x,l,r):
    if l>r:
        return -1
    m = (l+r)//2
    if arr[m][0]<=x:
        ans1 = binaryRight(arr,x,m+1,r)
        if ans1!=-1:
            return ans1
        else:
            return m
    else:
        return binaryRight(arr,x,l,m-1)
import bisect

t = int(inputmethod())
for _ in range(t):
    n = int(inputmethod())
    arr = [*map(int,inputmethod().split(' '))]

    arr2 = [[]]*n
    for i,x in enumerate(arr):
        arr2[i] = [x,i]

    arr2.sort()

    cumu = [0]
    for x,i in arr2:
        cumu.append(cumu[-1]+x)

    ans = []
    for i in range(n):
        score = arr2[i][0] # initial score

        score = cumu[i+1]
        count = i
        j = i

        while(True):
            jNew = bisect.bisect_right(arr2,[score,n])-1
            if jNew==j or jNew==-1:
                break

            j = jNew
            score = cumu[j+1]
            count = j

        ans.append(count)

    ans2 = [-1]*n
    for j,(x,i) in enumerate(arr2):
        ans2[i] =ans[j]

    ansStrMap = map(str,ans2)
    ansStr = ' '.join(ansStrMap)
    print(ansStr)