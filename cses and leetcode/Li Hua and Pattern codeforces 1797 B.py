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
    n,k = [*map(int,inputmethod().split())]
    grid = []
    for _ in range(n):
        row = [*map(int,inputmethod().split())]
        grid.append(row)

    # if k>=n*n//2:
    #     print("YES")
    #     continue

    count = 0
    possible = True
    for y in range((n+1)//2):
        for x in range(n):
            if y==n-1-y and n-1-x<=x:
                break
            if grid[y][x]!=grid[n-1-y][n-1-x]:
                count+=1
                if count>k:
                    possible = False
                    break
        if not possible:
            break

    if not possible:
        print("NO")
    elif n%2==0 and (k-count)%2==1:
        print("NO")
    else:
        print("YES")