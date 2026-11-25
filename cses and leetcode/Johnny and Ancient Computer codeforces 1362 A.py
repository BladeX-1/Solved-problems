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


import math
from decimal import Decimal
t = int(inputmethod())
for _ in range(t):
    a,b = [*map(int,inputmethod().split())]
    small = min(a,b)
    big = max(a,b)

    small = Decimal(small)
    big = Decimal(big)

    power2 = big/small
    if int(power2)!=power2:
        print(-1)
        continue

    power2 = int(power2)

    if power2.bit_count()!=1:
        print(-1)
    else:
        lg = math.log2(power2)
        print(math.ceil(lg/3))