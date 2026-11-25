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
    n,c = inputmethod().split()
    n = int(n)
    s = inputmethod()

    if c=="g":
        print(0)
        continue

    l = None
    ans = 0
    for i in range(2*n):
        if l==None and s[i%n]==c:
            l = i
        if l!=None and s[i%n]=='g':
            if i-l>ans:
                ans = i-l
            l = None

    print(ans)