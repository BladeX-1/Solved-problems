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



t = int(inputmethod())
answers = []
for _ in range(t):
    n = int(inputmethod())
    arr = [*map(int,inputmethod().split(' '))]
    ans = 0
    for k in range(1,n+1):
        if n%k!=0:
            continue


        max_ = -float('inf')
        min_ = float('inf')
        for start in range(0,n-k+1,k):
            windowSum = 0
            for i in range(start,start+k):
                windowSum+=arr[i]
            max_ = max(max_,windowSum)
            min_ = min(min_,windowSum)
        ansTemp = max_-min_
        ans = max(ans,ansTemp)
    answers.append(str(ans))

print('\n'.join(answers))