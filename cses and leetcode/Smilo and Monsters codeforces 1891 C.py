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
    arr = [*map(int,inputmethod().split())]
    arr.sort()

    r = n-1
    l = 0
    x = 0
    count = 0
    while(l<r):
        temp = min(arr[l],arr[r]-x)
        x+=temp
        arr[l]-=temp
        count+=temp
        if arr[l]==0:
            l+=1
        if l<=r and x==arr[r]:
            # arr[r]-=x
            arr[r]-=x
            x=0
            r-=1
            count+=1

    # assert l==r, (l,r)
    if l<=r:
        assert x<=arr[l]

        k = (arr[l]-x)//2

        if k>0:
            count+=k
            x+=k
            arr[l]-=k

        if x>0:
            count+=1
            arr[l]-=x
            x=0

        count+=arr[l]


    print(count)