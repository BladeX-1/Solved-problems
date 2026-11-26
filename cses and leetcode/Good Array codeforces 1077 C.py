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
if n==2:
    print(0)
    exit()

sumArr = sum(arr)
maxArr = max(arr[:2])
maxArr2 = min(arr[:2])
for i in range(2,n):
    if arr[i]>=maxArr:
        maxArr2 = maxArr
        maxArr = arr[i]
    elif arr[i]>maxArr2:
        maxArr2 = arr[i]

nice = []
for i in range(n):
    if arr[i]!=maxArr and sumArr-arr[i]-maxArr==maxArr:
        nice.append(i+1)
    elif arr[i]==maxArr and sumArr-arr[i]-maxArr2==maxArr2:
        nice.append(i+1)

niceStrMap = map(str,nice)
niceStr = ' '.join(niceStrMap)

print(len(nice))
if len(nice)>0:
    print(niceStr)