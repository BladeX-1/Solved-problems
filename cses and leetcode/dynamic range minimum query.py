import sys
try:
    open("__localsystemflag__").close()
    f = open('inp.txt')
    env = 'local'
except FileNotFoundError:
    inputArr = sys.stdin.read().split('\n')
    inputI = [0]
    f = None
    env = 'server'


def inputmethod():
    if f:
        return f.readline().strip()
    else:
        inputI[0]+=1
        return inputArr[inputI[0]-1]



n,q = [*map(int,inputmethod().split(' '))]
arr = [*map(int,inputmethod().split(' '))]

segment = [-1]*(4*n) ### ????????????? try this
segmentZero = -1

def build(i,arrL,arrR):
    global segmentZero
    if arrL==arrR:
        segment[i] = arr[arrL]
        return
    arrM = (arrL+arrR)//2
    build(i*2+1,arrL,arrM)
    build(i*2+2,arrM+1,arrR)
    segment[i] = min(segment[i*2+1],segment[i*2+2])


def query(i,segL,segR,arrL,arrR):
    if arrL<=segL and segR<=arrR:
        return segment[i]
    elif arrR<segL or segR<arrL:
        return float('inf')

    segM = (segL+segR)//2
    left = query(i*2+1,segL,segM,arrL,arrR)
    right = query(i*2+2,segM+1,segR,arrL,arrR)

    return min(left,right)

def update(i,newValue,k,l,r):
    if l==r==k:
        segment[i] = newValue
        return newValue
    elif l==r:
        assert False

    m = (l+r)//2
    if k<=m:
        childMin = update(2*i+1,newValue,k,l,m)
    else:
        childMin = update(2*i+2,newValue,k,m+1,r)

    segment[i] = min(segment[2*i+1],segment[2*i+2])
    return childMin

build(0,0,n-1)


ansarr = []
for _ in range(q):
    code,a,b = [*map(int,inputmethod().split(' '))]

    if code==1:
        update(0,b,a-1,0,n-1)
        # print('seg',segment)
    else:
        ans = query(0,0,n-1,a-1,b-1)
        ansarr.append(str(ans))

print(' '.join(ansarr))