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
    l=-1
    r = n

    alice = 0
    bob = 0
    candyCount = 0
    ans = 0
    while(l+1<r):
        if alice<=bob:
            alice+=arr[l+1]
            l+=1
            candyCount+=1
        else:
            bob+=arr[r-1]
            r-=1
            candyCount+=1

        if alice==bob:
            ans = candyCount

    print(ans)