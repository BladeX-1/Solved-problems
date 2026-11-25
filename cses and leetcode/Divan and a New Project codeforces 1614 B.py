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
    ans = [0]*(n+1)
    arr2 = [[]]*n
    for i in range(n):
        arr2[i] = [arr[i],i]
    arr2.sort(reverse=True)
    walk = 0
    temp = 1
    for i in range(0,n,2):
        walk+=temp*arr2[i][0]
        ans[i+1] = temp
        if i+2<n+1:
            walk+=temp*arr2[i+1][0]
            ans[i+2] = -temp
        temp+=1
    walk*=2

    finalAns = [0]*(n+1)
    for i in range(n):
        finalAns[arr2[i][1]+1] = ans[i+1]
    ansStrMap = map(str,finalAns)
    ansStr = ' '.join(ansStrMap)
    print(walk)
    print(ansStr)