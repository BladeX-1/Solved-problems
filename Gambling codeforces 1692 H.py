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


from collections import defaultdict as dd
t = int(inputmethod())
for _ in range(t):
    n = int(inputmethod())
    arr = [*map(int,inputmethod().split())]

    x2is = dd(list)
    for i in range(n):
        x2is[arr[i]].append(i)

    maxGap = -1
    lGap = -1
    rGap = -1
    for x in x2is:
        ies = x2is[x]
        temp = []
        for i in range(len(ies)):
            temp.append(2*i-ies[i])

        l = 0
        r = 0
        tempGap = -1
        for i in range(len(temp)):
            if temp[i]<temp[l]:
                l = i
            elif temp[i]-temp[l]>tempGap:
                r = i
                tempGap = temp[i]-temp[l]
        if tempGap>maxGap:
            maxGap = tempGap
            lGap = l
            rGap = r
