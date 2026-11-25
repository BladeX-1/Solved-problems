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
for _ in range(t):
    n,x = [*map(int,inputmethod().split())]
    foods = [*map(int,inputmethod().split())]

    min_ = foods[0]
    max_ = foods[0]
    changes = 0
    for i in range(1,n):
        newMin = min(min_,foods[i])
        newMax = max(max_,foods[i])

        if newMax-newMin>2*x:
            changes += 1
            min_ = foods[i]
            max_ = foods[i]
        else:
            min_ = newMin
            max_ = newMax

    print(changes)