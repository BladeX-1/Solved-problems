import sys
inputI = -1
inputArr = []
spliter = "\n"
try:
    open("__localsystemflag__").close()
    f = open('inp.txt')
    env = 'local'
except FileNotFoundError:
    rawInput = sys.stdin.read()
    inputArr = rawInput.splitlines()
    
    inputI = 0
    f = None
    env = 'server'

def inputmethod():
    global inputI
    if f:
        return f.readline().strip()
    else:
        inputI+=1
        return inputArr[inputI-1]
        return input()


import math

t = int(inputmethod())
for _ in range(t):
    n = int(inputmethod())
    arr = [*map(int,inputmethod().split())]


    arrType0 = arr[::2]
    arrType1 = arr[1::2]
    gcdArrType0 = math.gcd(*arrType0)
    gcdArrType1 = math.gcd(*arrType1)

    if gcdArrType0 == gcdArrType1:
        print(0)
        continue

    possible = True
    for i in range(len(arrType0)):
        if arrType0[i]%gcdArrType1==0:
            possible = False
            break

    if possible:
        print(gcdArrType1)
        continue

    possible = True
    for i in range(len(arrType1)):
        if arrType1[i]%gcdArrType0==0:
            possible = False
            break

    if possible:
        print(gcdArrType0)
        continue

    print(0)