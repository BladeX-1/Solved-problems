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
t = int(inputmethod())
for _ in range(t):
    n = int(inputmethod())
    arr1 = [*map(int,inputmethod().split())]
    arr2 = [*map(int,inputmethod().split())]

    x2len = dd(int)

    l = 0
    for i in range(n):
        if i==0 or arr1[i-1]!=arr1[i]:
            l = i
        if i==n-1 or arr1[i]!=arr1[i+1]:
            x2len[arr1[i]] = max(x2len[arr1[i]],i-l+1)

    l = 0
    ans = max(x2len.values())
    for i in range(n):
        if i==0 or arr2[i-1]!=arr2[i]:
            l = i
        if (i==n-1 or arr2[i]!=arr2[i+1]):
            ans = max(ans,i-l+1+x2len[arr2[i]])

    print(ans)