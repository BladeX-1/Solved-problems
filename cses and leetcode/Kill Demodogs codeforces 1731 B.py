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


M = 10**9+7
t = int(inputmethod())
for _ in range(t):
    n = int(inputmethod())

    evens = (n*(n+1)*(2*n+1)//6)%M
    k = (2*n-1)//2
    odds = (k*(k+1)*(2*k+1)//6+k*(k+1)//2)%M

    ans = evens+odds
    print((ans*2022)%M)