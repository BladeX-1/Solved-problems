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
    l=0
    r=n-1
    while(l<r and arr[l]==arr[r]):
        l+=1
        r-=1

    if l>=r:
        print("YES")
        continue

    possibles = [arr[l],arr[r]]

    isPalin = True
    for p in possibles:
        l=0
        r=n-1
        isPalin = True
        while(l<r):
            while(arr[l]==p and l<r):
                l+=1
            while(arr[r]==p and l<r):
                r-=1
            if l>=r:
                break
            if arr[l]!=arr[r]:
                isPalin = False
                break
            l+=1
            r-=1

        if isPalin:
            print("YES")
            break

    if not isPalin:
        print("NO")