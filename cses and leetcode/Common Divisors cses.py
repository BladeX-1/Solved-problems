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



n = int(inputmethod())
arr = [*map(int,inputmethod().split())]
from collections import Counter
c = Counter(arr)
g = 1
for k,v in c.items():
    if v>=2:
        g = max(g,k)

arrSet = set(c.keys())

maxArr = max(arr)
found = False
for i in reversed(range(g+1,maxArr//2+1)):
    count = 0
    multiple = i
    while(multiple<=maxArr):
        if multiple in arrSet:
            count+=1
            if count==2:
                g = i
                found = True
                break
        multiple+=i

    if found:
        break

print(g)