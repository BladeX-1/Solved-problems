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


def myLog(n,k):
    ans = 0
    while(n):
        n//=k
        ans+=1
    return ans
t = int(inputmethod())
for _ in range(t):
    a,b = [*map(int,inputmethod().split())]
    extra = 0
    if b==1:
        b+=1
        extra = 1
    ans = 10+a
    for i in range(100):
        temp = myLog(a,b+i)
        if i+extra>=ans:
            break
        ans = min(ans,extra+i+temp)

    print(ans)