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



t = int(inputmethod())
for _ in range(t):
    ylen,xlen = [*map(int,inputmethod().split())]
    grid = []
    rowReachOld = []
    solved = False
    for y in range(ylen):
        rowReachCurrent = []
        row = [*map(int,inputmethod().split())]
        for x in range(xlen):
            if y==0 and x==0:
                rowReachCurrent.append(set())
                rowReachCurrent[-1].add(row[0])
                continue

            temp = set()
            if rowReachOld:
                temp|=rowReachOld[x]
            if len(rowReachCurrent)>=1:
                temp|=rowReachCurrent[-1]

            rowReachCurrent.append(set())
            if temp:
                manhatan = ylen-1+xlen-1-y-x
                for old in temp:
                    new = old+row[x]
                    if abs(new)>manhatan:
                        continue
                    rowReachCurrent[-1].add(new)

        

        rowReachOld = rowReachCurrent

        if y==ylen-1 and (0 in rowReachCurrent[-1]):
            solved = True
            break
    if solved:
        print("YES")
    else:
        print("NO")
