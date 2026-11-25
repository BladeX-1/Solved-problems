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
    n,k,q = [*map(int,inputmethod().split())]
    arrMap = map(int,inputmethod().split())
    arr2 = [*map(lambda x:x<=q,arrMap)]

    intervals = []
    l = -1
    ans = 0
    for i in range(n):
        if i==0 or arr2[i-1]==False and arr2[i]==True:
            l = i

        if arr2[i]==True and i-l+1>=k:
            ans+=i-l+1-k+1

    print(ans)