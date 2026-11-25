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
# mods = []
def getNonZeroDigits(n):
    ans = set(map(int,str(n)))
    if 0 in ans:
        ans.remove(0)
    if 1 in ans:
        ans.remove(1)
    return list(ans)

for _t in range(t):
    n = int(inputmethod())
    for i in range(n,n+3000):
        digits = getNonZeroDigits(i)
        works = True
        for d in digits:
            if i%d!=0:
                works = False
                break
        if works:
            print(i)
            break