import sys
inputI_23235231253 = -1
inputArr_6273468273 = []
spliter = "\n"
try:
    open("__localsystemflag__").close()
    file_input_txt_2342349 = open('inp.txt')
    env = 'local'
except FileNotFoundError:
    rawInput = sys.stdin.read()
    inputArr_6273468273 = rawInput.splitlines()
    
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

import math


segmentTreeGCD = []
def buildSegmentTreeGCD(segmentTree,i,arr,arrL,arrR):
    # if arrR<arrL:
    #     segmentTree[i] = 0
    #     return 0
    if arrL==arrR:
        segmentTree[i] = arr[arrL]
        return arr[arrL]
    
    left = 2*i+1
    right = 2*i+2
    arrM = (arrL+arrR)//2
    if arrL<=arrM:
        buildSegmentTreeGCD(segmentTree,left,arr,arrL,arrM)
    if arrM+1<=arrR:
        buildSegmentTreeGCD(segmentTree,right,arr,arrM+1,arrR)
    segmentTree[i] = math.gcd(segmentTree[left],segmentTree[right])

def queryGCD(segmentTree,i,arr,segL,segR,arrL,arrR):
    if arrL<=segL and segR<=arrR:
        return segmentTree[i]
    elif segR<arrL or arrR<segL:
        return 0

    segM = (segL+segR)//2
    gcdLeft = queryGCD(segmentTree,2*i+1,arr,segL,segM,arrL,arrR)
    gcdRight = queryGCD(segmentTree,2*i+2,arr,segM+1,segR,arrL,arrR)
    return math.gcd(gcdLeft,gcdRight)


t = int(inputmethod())
for _ in range(t):
    n,q = [*map(int,inputmethod().split())]
    arr = [*map(int,inputmethod().split())]

    arrPairs = []
    for i in range(n-1):
        arrPairs.append(abs(arr[i+1]-arr[i]))

    segmentTreeGCD = [0]*(4*n)
    buildSegmentTreeGCD(segmentTreeGCD,0,arrPairs,0,len(arrPairs)-1)

    answersStr = []
    for _q in range(q):
        l,r = [*map(int,inputmethod().split())]
        l-=1
        r-=1
        if l==r:
            ans = 0
        else:
            ans = queryGCD(segmentTreeGCD,0,arrPairs,0,len(arrPairs)-1,l,r-1)
        assert ans>=0
        answersStr.append(str(ans))
    print(' '.join(answersStr))
    # del answersStr,segmentTreeGCD,arrPairs