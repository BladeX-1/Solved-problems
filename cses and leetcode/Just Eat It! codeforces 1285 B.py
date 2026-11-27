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
    n = int(inputmethod())
    arr = [*map(int,inputmethod().split())]

    cumu = [0]
    for x in arr:
        cumu.append(cumu[-1]+x)

    l = cumu[0]
    maxRangeValue = cumu[0]
    for ri in range(n):
        r = cumu[ri]
        if r-l>maxRangeValue:
            maxRangeValue = r-l
        if r<l:
            l = r
    l = cumu[1]
    for ri in range(1,n+1):
        r = cumu[ri]
        if r-l>maxRangeValue:
            maxRangeValue = r-l
        if r<l:
            l = r

    sumArr = sum(arr)

    if sumArr>maxRangeValue:
        print("YES")
    else:
        print('NO')