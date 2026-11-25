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
for _ in range(t):
    n,r,b = [*map(int,inputmethod().split(' '))]

    # b<r

    buckets = b+1
    minInBucket = r//buckets
    extra = r%buckets

    arr = []
    for i in range(buckets):
        arr.append('R'*minInBucket)
        if i<extra:
            arr.append('R')
        if i!=buckets-1:
            arr.append('B')

    ans = ''.join(arr)
    assert len(ans)==n
    print(ans)