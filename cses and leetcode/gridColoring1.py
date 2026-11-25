import sys
sys.setrecursionlimit(500*500+2)

# f = open('inp.txt')
def inputmethod():
    return input()
    # return f.readline().strip()

ylen,xlen = [*map(int,inputmethod().split(' '))]
grid = []
for _ in range(ylen):
    row = list(inputmethod())
    grid.append(row)

gridAns = [[None]*xlen for _ in range(ylen)]

def getNextYX(y,x,ylen,xlen):
    x+=1
    y+=x//xlen
    x%=xlen
    return y,x

allChars = "ABCD"
allCharsSet = set(allChars)

def bt(grid,gridAns,y,x,ylen,xlen):
    if y==ylen:
        return True
    
    possibles = allCharsSet.copy()
    if y!=0 and gridAns[y-1][x] in possibles:
        possibles.remove(gridAns[y-1][x])
    if x!=0 and gridAns[y][x-1] in possibles:
        possibles.remove(gridAns[y][x-1])
    
    if grid[y][x] in possibles:
        possibles.remove(grid[y][x])

    

    for c in possibles:
        gridAns[y][x] = c
        ans = bt(grid,gridAns,*getNextYX(y,x,ylen,xlen),ylen,xlen)
        if ans:
            return True
        gridAns[y][x] = None

    return False
solved = bt(grid,gridAns,0,0,ylen,xlen)
if not solved:
    print("IMPOSSIBLE")
else:
    for row in gridAns:
        print(''.join(row))
