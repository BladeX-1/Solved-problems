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


from collections import deque
t = int(inputmethod())
for _ in range(t):
    n,p = [*map(int,inputmethod().split())]
    arr = [*map(int,inputmethod().split())]
    brr = [*map(int,inputmethod().split())]

    arr2 = []
    for i in range(n):
        arr2.append([brr[i],arr[i]])

    arr2.sort()
    print(arr2)


    ans = 0
    heard = deque()

    l = 0

    r = n-1
    while(l<=r):
        if arr2[l][0]<p:
            ans+=p
            cost,reach = arr2[l]
            l+=1

            ans+=min(r-l+1,reach)*cost
            r-=min(r-l+1,reach)
        else:
            break

    if l<=r:
        ans+=p*(r-l+1)
    print(ans)