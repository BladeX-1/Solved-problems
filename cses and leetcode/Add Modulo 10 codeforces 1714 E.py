import sys
inputI_23235231253 = -1
inputArr_6273468273 = []
spliter = "\n"
try:
    open("__localsystemflag__").close()
    file_input_txt_2342349 = open('inp.txt')
    env = 'local'
except FileNotFoundError:
    rawInput = sys.stdin.read()
    inputArr_6273468273 = rawInput.splitlines()
    
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


# 1 2 4 8 16 22;  2;  3 6;  4;  5 10 10;  6;   7 14;  8;  9 18; 10 10;


t = int(inputmethod())
loops2 = set([2,4,8,6])
# loops10 = 0
for _t in range(t):
    n = int(inputmethod())
    arr = [*map(int,inputmethod().split())]

    fives = 0
    for i in range(n):
        if arr[i]%5==0:
            fives+=1
            if arr[i]%10==5:
                arr[i]+=arr[i]%10

    # handle %5=0 cases
    possible = True
    if 0<fives<n:
        print("NO")
        continue
    elif fives==n:
        for i in range(n-1):
            if arr[i]!=arr[i+1]:
                possible = False
                break
        if possible:
            print("YES")
            continue

    if not possible:
        print('NO')
        continue

    d = {1:1,2:0,3:3+6,4:4+8+6,6:6,7:7+4+8+6,8:8+6,9:9+8+6}
    for i in range(n):
        arr[i]+=d[arr[i]%10]

    maxArr = max(arr)
    possible = True
    for i in range(n):
        arr[i]+=20*((maxArr-arr[i])//20)
        if i>0:
            if arr[i-1]!=arr[i]:
                possible = False
                break
        

    if not possible:
        print("NO")
    else:
        print("YES")