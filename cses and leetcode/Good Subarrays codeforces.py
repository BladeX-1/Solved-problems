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


from collections import defaultdict as dd
t = int(inputmethod())
for _ in range(t):
    n = int(inputmethod())
    arr = [*map(int,inputmethod())]
    cumu = [0]
    for i in range(n):
        cumu.append(cumu[-1]+arr[i])

    cumu2 = []
    j = n-1
    for i in range(n+1):
        cumu2.append(j+cumu[i])
        j-=1

    past = dd(int)
    ans = 0
    for c in cumu2:
        ans+=past[c]
        past[c]+=1

    print(ans)