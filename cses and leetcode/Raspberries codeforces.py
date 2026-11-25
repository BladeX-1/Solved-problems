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


from collections import Counter

t = int(inputmethod())
for _ in range(t):
    n,k = [*map(int,inputmethod().split(' '))]
    arr1Map = map(int,inputmethod().split(' '))

    arr2Map = map(lambda x:x%k,arr1Map)
    c = Counter(arr2Map)

    if k!=4:
        for i in range(k):
            if c[(k-i)%k]>0:
                print(i)
                break
    else:
        if c[0]>0 or c[2]>=2:
            print(0)
        elif c[3]>0:
            print(1)
        elif c[2]==1:
            if c[1]>0 or c[3]>0:
                print(1)
            else:
                print(2)
        elif c[1]>=2:
            print(2)
        elif c[1]==1:
            print(3)
        else:
            assert False