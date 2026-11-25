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



n,k = [*map(int,inputmethod().split(' '))]

deletedInRangeTree = [0]*(4*n)
# def build(arrL,arrR,i):
#     if arrL>arrR:
#         return
#     arrM = (arrL+arrR)//2
#     build(arrL,arrM,2*i+1)
#     build(arrM+1,arrR,2*i+2)
#     deletedInRangeTree[i] = deletedInRangeTree[2*i+1]+deletedInRangeTree[2*i+2]

def update(i,arrL,arrR,arrI):
    if arrL>arrR:
        return
    if arrL<=arrI<=arrR:
        deletedInRangeTree[i]+=1
        arrM = (arrL+arrR)//2
        if arrI<=arrM:
            update(2*i+1,arrL,arrM,arrI)
        else:
            update(2*i+2,arrM+1,arrR,arrI)

def query(i,arrL,arrR,treeL,treeR):
    if treeL<=arrL and arrR<=treeR:
        return deletedInRangeTree[i]
    elif arrR<treeL or treeR<arrL:
        return 0

    treeM = (treeL+treeR)//2
    return query(2*i+1,arrL,arrR,treeL,treeM)+query(2*i+1,arrL,arrR,treeM+1,treeR)

i=-1
left = n
while(left>1):
    tempK = k%left
    i += 
    left -= 1