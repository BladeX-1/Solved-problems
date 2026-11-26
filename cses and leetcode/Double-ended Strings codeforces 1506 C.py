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


t = int(inputmethod())
for _ in range(t):
    a = inputmethod()
    b = inputmethod()

    lenA = len(a)
    allAes = set([''])
    for l in range(lenA):
        for r in range(l,lenA):
            allAes.add(a[l:r+1])

    allBes = set([''])
    for l in range(len(b)):
        for r in range(l,len(b)):
            allBes.add(b[l:r+1])

    temp = max(map(len,(allAes & allBes)))
    ans = len(a)+len(b)-temp-temp
    print(ans)