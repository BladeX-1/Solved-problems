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
    arr = [*map(int,inputmethod().split())]

    size2i = dd(list)
    for i in range(n):
        size2i[arr[i]].append(i+1)

    possible = True
    ans = [-1]*n
    for size_,inds in size2i.items():
        if len(inds)==1:
            possible = False
            break
        for i in range(len(inds)):
            ans[inds[i]-1] = inds[(i+1)%len(inds)]


    if not possible:
        print(-1)
    else:
        strMap = map(str,ans)
        print(' '.join(strMap))