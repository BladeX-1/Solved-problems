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

def rot90(grid):
    n = len(grid)
    newGrid = [[-1]*n for _ in range(n)]

    for y in range(n):
        for x in range(n):
            newGrid[x][n-1-y] = grid[y][x]

    return newGrid

t = int(inputmethod())
for _ in range(t):
    n = int(inputmethod())
    grid = []
    for __ in range(n):
        row = [*map(int,list(inputmethod()))]
        assert len(row)==n
        grid.append(row)

    assert len(grid)==n
    grid90 = rot90(grid)
    grid180 = rot90(grid90)
    grid270 = rot90(grid180)

    # for row in grid:
    #     print(row)
    # print()
    # for row in grid90:
    #     print(row)
    # print()

    flips = 0
    for y in range(n//2):
        for x in range(n//2):
            zeroOne = [0,0]
            for i in [grid[y][x],grid90[y][x],grid180[y][x],grid270[y][x]]:
                zeroOne[i]+=1
            assert sum(zeroOne)==4
            flips+=min(zeroOne)

    # print('flips 1',flips) # found correct
    if n%2==1:
        x = n//2
        for y in range(n//2):
            zeroOne = [0,0]
            for i in [grid[y][x],grid90[y][x],grid180[y][x],grid270[y][x]]:
                zeroOne[i]+=1
            assert sum(zeroOne)==4
            flips+=min(zeroOne)

    print(flips)