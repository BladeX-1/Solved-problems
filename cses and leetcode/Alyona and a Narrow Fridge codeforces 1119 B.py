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



n,h = [*map(int,inputmethod().split())]
arr = [*map(int,inputmethod().split())]
arr2 = []
for i in range(n):
    arr2.append([arr[i],i])
arr2.sort(reverse=True)


def tryFilling(height,arr):
    filled = 0
    for i in range(len(arr)-1,-1,-2):
        if arr[i]+filled<=height:
            filled+=arr[i]
        else:
            return False,-1
    return True,filled

lower = 0
upper = n-1
oldLower = 0
ans = 0
while(lower<=upper):
    mid = (upper+lower)//2
    arrCopy = arr[oldLower:mid+1]
    arrCopy.sort()
    isFilled,moreHeightFilled = tryFilling(h,arrCopy)
    if isFilled:
        ans = mid+1
        lower = mid+1
    else:
        upper = mid-1

print(ans)