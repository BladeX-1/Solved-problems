import sys
inputI = -1
inputArr = []
try:
    open("__localsystemflag__").close()
    f = open('inp.txt')
    env = 'local'
except FileNotFoundError:
    inputArr = sys.stdin.read().split('\n')
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


n = int(inputmethod())
grid = []
for _ in range(n):
    s = inputmethod()
    grid.append(s)

from collections import deque
from collections import defaultdict as dd
def grid_bfs(grid):
    # def bfs_grid(grid,y,x):

    ylen = len(grid)
    xlen = len(grid[0])

    visited = [[False]*xlen for _ in range(ylen)]

    dx = [0, 1]
    dy = [1, 0]

    # def isBounded(y_,x_,ylen,xlen):
    def isBounded(y_, x_):
        return 0 <= y_ < ylen and 0 <= x_ < xlen

    qsuper = deque([[0, 0]])
    q = deque()
    visited[0][0] = True
    ans = []
    lowest = grid[0][0]
    while q or qsuper:
        if not q:
            ans.append(lowest)
            q = qsuper
            qsuper = deque()
            lowest = 'Z'

        topY, topX = q.pop()

        for i in range(2):
            ynew = topY + dy[i]
            xnew = topX + dx[i]

            if not isBounded(ynew, xnew):
                continue
            if visited[ynew][xnew]:
                continue
            if grid[ynew][xnew]<lowest:
                lowest = grid[ynew][xnew]

        for i in range(2):
            ynew = topY + dy[i]
            xnew = topX + dx[i]

            if not isBounded(ynew, xnew):
                continue
            if visited[ynew][xnew]:
                continue
            visited[ynew][xnew] = True
            if grid[ynew][xnew]==lowest:
                qsuper.append([ynew, xnew])

    return ''.join(ans)



ans = grid_bfs(grid)
print(ans)