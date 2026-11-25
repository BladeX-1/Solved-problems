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
for _t in range(t):
    n = int(inputmethod())
    firstArr = []
    secondArr = []

    for _ in range(n):
        m = int(inputmethod())
        arr = [*map(int,inputmethod().split())]
        first = min(arr[:2])
        second = max(arr[:2])

        for i in range(2,m):
            if arr[i]<=first:
                second = first
                first = arr[i]
            elif arr[i]<=second:
                second = arr[i]

        firstArr.append(first)
        secondArr.append(second)

    ans = sum(secondArr)-min(secondArr)+min(firstArr)
    print(ans)