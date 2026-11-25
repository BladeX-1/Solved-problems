import sys
inputI_23235231253 = -1
inputArr_6273468273 = []
try:
    open("__localsystemflag__").close()
    file_input_txt_2342349 = open('inp.txt')
    env = 'local'
except FileNotFoundError:
    rawInput_568279834 = sys.stdin.read()
    inputArr_6273468273 = rawInput_568279834.splitlines()
    
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

from collections import defaultdict as dd

t = int(inputmethod().strip())
for _ in range(t):
    n = int(inputmethod().strip())
    arr = [*map(int,inputmethod().strip().split())]

    cumu__ = [0]
    for x in arr:
        cumu__.append(cumu__[-1]+x)

    allSum = dd(list)
    for l in range(n+1):
        for r in range(l+1,n+1):
            temp = cumu__[r]-cumu__[l]
            allSum[temp].append([l,r])

    if duplicate__:
        print("YES")
    else:
        print("NO")
