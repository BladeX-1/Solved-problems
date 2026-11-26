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



n,q = [*map(int,inputmethod().split())]
cards = [*map(int,inputmethod().split())]
queries = [*map(int,inputmethod().split())]

null=n+100
topMost = [null]*51
for i in range(n):
    if topMost[cards[i]]==null:
        topMost[cards[i]] = i+1

ans = []
for q in queries:
    temp = topMost[q]
    ans.append(str(temp))
    for i in range(1,51):
        if topMost[i]<temp:
            topMost[i]+=1
    topMost[q] = 1

print(' '.join(ans))