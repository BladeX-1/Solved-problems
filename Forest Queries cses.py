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



n,q = [*map(int,inputmethod().split())]
cumu = [[0]*(n+1) for _ in range(n)]
cumu2 = [[0]*(n+1) for _ in range(n+1)]

for y in range(n):
    row = inputmethod()
    temp = 0
    for x in range(n):
        if row[x]=='*':
            temp+=1
        cumu[y][x+1] = temp

for x in range(n):
    temp = 0
    for y in range(n):
        temp+=cumu[y][x+1]
        cumu2[y+1][x+1] = temp

for _ in range(q):
    y1,x1,y2,x2 = [*map(int,inputmethod().split())]
    ans = cumu2[y2][x2]-cumu2[y1-1][x2]-(cumu2[y2][x1-1]-cumu2[y1-1][x1-1])
    print(ans)