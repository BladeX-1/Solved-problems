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


n = int(inputmethod())
intervals = []
for _n in range(n):
    l,r = [*map(int,inputmethod().split())]
    intervals.append([l,r])

intervals.sort()
firstEnds = -1
secondEnds = -1
possible = True
for l,r in intervals:
    if firstEnds<l:
        firstEnds = r
    elif secondEnds<l:
        secondEnds = r
    else:
        possible = False
        break

if possible:
    print('YES')
else:
    print("NO")