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





import bisect

t = int(inputmethod())
for _ in range(t):
    n = int(inputmethod())
    arr = [*map(int,inputmethod().split())]

    cumuXor = [0]
    for x in arr:
        cumuXor.append(cumuXor[-1]^x)


    leftSetsCumu = [[0]*32]
    rightSetsCumu = [[0]*32]

    for i in range(1,n+1):
        temp = cumuXor[i]
        leftSetsCumu.append(leftSetsCumu[-1][:])
        for j in range(32):
            if (temp>>j)==0:
                break
            if (temp>>j)&1==1:
                leftSetsCumu[i][j] += 1
    leftSetsCumu.pop(0)

    for i in reversed(range(n)):
        temp = cumuXor[n]^cumuXor[i]
        rightSetsCumu.append(rightSetsCumu[-1][:])
        for j in range(32):
            if (temp>>j)==0:
                break
            if (temp>>j)&1==1:
                rightSetsCumu[-1][j]+=1
    rightSetsCumu.pop(0)
    rightSetsCumu.reverse()

    ans = 0
    for i in range(n):
        j = arr[i].bit_length()-1
        assert j>=0
        ans += rightSetsCumu[i][j]*leftSetsCumu[i][j] - 1
        ans += (n-1-(i-1)-rightSetsCumu[i][j])*(i+1-leftSetsCumu[i][j])

    print(ans)