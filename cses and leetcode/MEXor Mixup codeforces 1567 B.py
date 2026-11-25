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


def xor_0_to_n(n):
    return [n,1,n+1,0][n%4]

t = int(inputmethod())
for _ in range(t):
    a,b = [*map(int,inputmethod().split())]

    temp = xor_0_to_n(a-1)
    count = a

    if temp==b:
        print(count)
        continue

    newNumber = temp^b
    if newNumber!=a:
        print(count+1)
        continue

    else:
        print(count+2)