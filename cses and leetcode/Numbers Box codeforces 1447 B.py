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
    ylen,xlen = [*map(int,inputmethod().split())]
    negatives = 0
    arr = []
    for y in range(ylen):
        row = [*map(int,inputmethod().split())]
        for x in row:
            if x<0:
                negatives+=1
        row = [*map(abs,row)]
        arr.extend(row)

    negatives%=2

    if negatives==1:
        sumArr = sum(arr)
        minArr = min(arr)
        ans = sumArr-2*minArr
        print(ans)
    else:
        print(sum(arr))