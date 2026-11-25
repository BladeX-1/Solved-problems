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


n,q = [*map(int,inputmethod().split(' '))]
arr = [*map(int,inputmethod().split(' '))]
inf=float('inf')
segmentTreeMinimum = [inf]*(4*n)

def fillTree(segment,arr,arrl,arrr,i):
    if arrl==arrr:
        segment[i] = arr[arrl]
        return
    arrm = (arrl+arrr)//2
    fillTree(segment,arr,arrl,arrm,i*2+1) # towards left child
    fillTree(segment,arr,arrm+1,arrr,i*2+2) # towards right child

    segment[i] = min(segment[2*i+1],segment[2*i+2])

def getMin(segment,i,arrl,arrh,segl,segh):
    if arrl<=segl and segh<=arrh:
        return segment[i]
    elif arrh<segl or segh<arrl:
        return float('inf')

    mid = (segl+segh)//2
    left = getMin(segment,2*i+1,arrl,arrh,segl,mid)
    right = getMin(segment,2*i+2,arrl,arrh,mid+1,segh)
    return min(left,right)

fillTree(segmentTreeMinimum,arr,0,n-1,0)
# print(segmentTreeMinimum)

ansarr = []
for _ in range(q):
    a,b = [*map(int,inputmethod().split(' '))]
    ans = getMin(segmentTreeMinimum,0,a-1,b-1,0,n-1)
    # print(a,b,'ans',ans)
    ansarr.append(ans)

print(*ansarr)