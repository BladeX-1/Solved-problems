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
    x,y,k = [*map(int,inputmethod().split())]

    maxSticks = y*k+k
    if (maxSticks-1)%(x-1)==0:
        temp = (maxSticks-1)//(x-1)
    else:
        temp = (maxSticks-1)//(x-1)+1
    moves = temp+k
    print(moves)