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


import itertools
import functools

t = int(inputmethod())
for _ in range(t):
    n,x,y = [*map(int,inputmethod().split())]
    arrMap = map(int,inputmethod().split())

    bit = functools.reduce(lambda e1,e2:(e1&1)^(e2&1),itertools.chain(arrMap,[x,y]))

    # bit = 0
    # for ele in arr:
    #     bit^=ele&1

    # bit^=x&1
    # bit^=y&1

    if bit==0:
        print("Alice")
    elif bit==1:
        print("Bob")