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



t = int(inputmethod())
for _ in range(t):
    n,k,z = [*map(int,inputmethod().split())]
    z = min(k//2,z)
    arr = [*map(int,inputmethod().split())]
    pairs = []
    for i in range(n-1):
        pairs.append(arr[i]+arr[i+1])

    temp = pairs[0]
    maxPairs = [temp]
    for i in range(1,len(pairs)):
        temp = max(temp,pairs[i])
        maxPairs.append(temp)


    cumu = [0]
    for x in arr:
        cumu.append(cumu[-1]+x)

    ans = cumu[k+1]
    for extras in range(1,z*2+1):
        temp = cumu[k-extras+1] ## right
        if extras%2==1:
            temp+=arr[k-extras-1]
        if k-1-extras>=0 and extras>=2:
            temp+=maxPairs[k-1-extras]*(extras//2)

        ans=max(ans,temp)
    print(ans)