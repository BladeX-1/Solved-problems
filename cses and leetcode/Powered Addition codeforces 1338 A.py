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


import math
t = int(inputmethod())
for _t in range(t):
    n = int(inputmethod())
    arr = [*map(int,inputmethod().split())]

    maxX = 0
    for i in range(1,n):
        # print(arr)
        if arr[i-1]>arr[i]:
            temp = math.floor(math.log2(arr[i-1]-arr[i]))
            maxX = max(maxX,temp+1)
            # arr[i]+=2**(temp)
            arr[i] = arr[i-1]

    print(maxX)