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

import math

t = int(inputmethod())
for _ in range(t):
    n,m = [*map(int,inputmethod().split())]

    nCopy = n

    twoPowers = 0
    while(n and n%2==0):
        twoPowers+=1
        n//=2

    fivePowers = 0
    while(n and n%5==0):
        fivePowers+=1
        n//=5

    updated = False
    k = 1
    while(twoPowers<fivePowers and 2*k<=m):
        k*=2
        twoPowers+=1
        updated = True

    while(fivePowers<twoPowers and 5*k<=m):
        k*=5
        fivePowers+=1
        updated = True


    while(10*k<=m):
        k*=10
        twoPowers+=1
        fivePowers+=1
        updated = True

    if not updated:
        print(nCopy*m)
        continue

    k*=(m//k)
    
    print(k*nCopy)