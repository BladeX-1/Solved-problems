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


import functools
t = int(inputmethod())
for _ in range(t):
    n,k = [*map(int,inputmethod().split())]
    arr = [*map(int,inputmethod().split())]

    arrAnd = functools.reduce(lambda x,y:x&y,arr)

    bitCount = [n]*31

    for i in range(n):
        for j in range(31):
            if (arr[i]>>j)==0:
                break
            if (arr[i]>>j)&1==1:
                bitCount[j]-=1

    mask = 0
    for j in reversed(range(31)):
        if bitCount[j]<=k:
            k-=bitCount[j]
            mask|=1<<j

            if k==0:
                break

    print(arrAnd|mask)