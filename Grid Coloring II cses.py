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



ylen,xlen = [*map(int,inputmethod().split())]
grid = []
for y in range(ylen):
    row = list(inputmethod())
    grid.append(row)

newGrid = [['']*xlen for _ in range(ylen)]
alls = 'ABC'
def bt(y,x):
    if y==ylen:
        return True

    for c in alls:
        if grid[y][x]==c:
            continue
        if y-1>=0 and newGrid[y-1][x]==c:
            continue
        if x-1>=0 and newGrid[y][x-1]==c:
            continue

        newGrid[y][x] = c
        isSolved = bt(y+(x+1)//xlen,(x+1)%xlen)
        if isSolved:
            return True
    return False

isSolved = bt(0,0)
if isSolved:
    for row in newGrid:
        print(''.join(row))

else:
    print("IMPOSSIBLE")