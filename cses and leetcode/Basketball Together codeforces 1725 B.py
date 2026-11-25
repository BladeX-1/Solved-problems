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



n,d = [*map(int,inputmethod().split())]
arr = [*map(int,inputmethod().split())]

arr.sort()

import bisect

i = bisect.bisect_left(arr,d+1)-1
ans = n-1-i
l = 0
r = i
import math
while(l<=r):
    temp = math.ceil((d+1)/arr[r])
    if l+temp-1>r:
        break
    l+=temp-1
    ans+=1
    r-=1
print(ans)