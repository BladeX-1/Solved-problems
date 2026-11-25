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
    n,a,b = [*map(int,inputmethod().split())]
    arr = [*map(int,inputmethod().split())]

    if a<=b:
        ans = b*(arr[0]-0)
        for i in range(1,n):
            ans+=(arr[i]-arr[i-1])*b

        ans+=arr[-2]*a

        print(ans)

    else:
        arr2 = []
        arr2.append(0)
        arr2.append(arr[0]*b)
        for i in range(1,n):
            arr2.append(arr2[-1]+(arr[i]-arr[i-1])*b)

        arr3 = [0]
        temp = 0
        for i in reversed(range(n)):
            temp+=arr[i]
            arr3.append(arr3[-1]+(temp-arr[i])*b)
        arr3.pop(0)
        arr3.append(temp*b)

        arr3.reverse()

        print(arr2)
        print(arr3)

        best = float('inf')
        for i in range(0,len(arr2)):
            temp = a*arr[i-1] if i>0 else 0
            if arr2[i]+arr3[i]+temp<best:
                best = arr2[i]+arr3[i]+temp

        print(best)