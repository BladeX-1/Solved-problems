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



n = int(inputmethod())
arr = [*map(int,inputmethod().split())]

cumuXor = [0]
for x in arr:
    cumuXor.append(cumuXor[-1]^x)

cumu2l = []
cumu3r = []
for i in range(n+1):
    cumu2l.append(cumuXor[i]*i)
    cumu3r.append(cumuXor[i]*(i+1))

sumCumu2l = [0]
for i in range(n+1):
    sumCumu2l.append(sumCumu2l[-1]+cumu2l[i])

ans = 0
for r in range(1,n+1):
    ans+=(cumu3r[r]*r-sumCumu2l[r-1])

print(ans)