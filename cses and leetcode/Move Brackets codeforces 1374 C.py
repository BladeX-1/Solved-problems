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



OPEN = '('
CLOSE = ')'
t = int(inputmethod())
for _ in range(t):
    n = int(inputmethod())
    s = inputmethod()
    ans = 0
    active = 0
    for c in s:
        if c==OPEN:
            active+=1
        elif c==CLOSE:
            active-=1
            if active==-1:
                active=0
                ans+=1

    print(ans)