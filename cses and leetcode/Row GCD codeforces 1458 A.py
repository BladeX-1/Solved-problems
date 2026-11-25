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

lenArr,lenBrr = [*map(int,inputmethod().split())]
arr = [*map(int,inputmethod().split())]
brr = [*map(int,inputmethod().split())]


for i in range(1,lenArr):
    arr[i]-=arr[0]
remainingGcd = math.gcd(*arr[1:])

answers = []
for i in range(lenBrr):
    gcd = math.gcd(arr[0]+brr[i],remainingGcd)
    answers.append(str(gcd))

print(' '.join(answers))