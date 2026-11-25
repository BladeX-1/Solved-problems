try:
    open("__localsystemflag__").close()
    f = open('inp.txt')
    env = 'local'
except FileNotFoundError:
    f = None
    env = 'server'

def inputmethod():
    if f:
        return f.readline().strip()
    else:
        return input()


ylen,xlen = map(int,inputmethod().split(' '))
grid = []
start = None
end = None
for y in range(ylen):
    row = inputmethod()
    if (not start) and "A" in row:
        start = (y,row.index('A'))
    if (not end) and 'B' in row:
        end = (y,row.index('B'))
    grid.append(row)

assert start!=None
assert end!=None

WALL = '#'
FLOOR = '.'
END = 'B'
START = 'A'

from collections import deque
import time

def grid_bfs(grid, y, x, yend, xend):
    # def bfs_grid(grid,y,x):

    ylen = len(grid)
    xlen = len(grid[0])

    visited = [[False]*xlen for _ in range(ylen)]
    visitedInv = [[False]*xlen for _ in range(ylen)]

    paths = [['']*xlen for _ in range(ylen)]
    pathsInv = [['']*xlen for _ in range(ylen)]

    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    dd = 'DRUL'


    q = deque([(y, x)])
    qinv = deque([(yend,xend)])
    
    visited[y][x] = True
    visitedInv[yend][xend] = True

    paths[0][0] = ''
    pathsInv[yend][xend] = ''

    assert grid[y][x] == START

    while q or qinv:
        if q:
            topY, topX = q.popleft()

            for i in range(4):
                ynew = topY + dy[i]
                xnew = topX + dx[i]
                dnew = dd[i]

                if not (0 <= ynew < ylen and 0 <= xnew < xlen):
                    continue
                if visited[ynew][xnew]:
                    continue
                if grid[ynew][xnew] == WALL:
                    continue
                if grid[ynew][xnew] == END:
                    return paths[y][x]+dnew
                if visitedInv[ynew][xnew]:
                    forward = paths[y][x]+dnew

                    backward = pathsInv[y][x]
                    backward = backward[::-1]
                    backward = backward\
                        .replace('U','u')\
                        .replace('R','r')\
                        .replace('D','d')\
                        .replace('L','l')\
                        .replace('u','D')\
                        .replace('r','L')\
                        .replace('d','U')\
                        .replace('l','R')\

                    return forward+backward
                        

                visited[ynew][xnew] = True
                paths[ynew][xnew] = paths[y][x]+dnew
                q.append((ynew, xnew))

        if qinv:
            topY, topX = qinv.popleft()
        
            for i in range(4):
                ynew = topY + dy[i]
                xnew = topX + dx[i]
                dnew = dd[i]

                if not (0 <= ynew < ylen and 0 <= xnew < xlen):
                    continue
                if visitedInv[ynew][xnew]:
                    continue
                if grid[ynew][xnew] == WALL:
                    continue
                # if grid[ynew][xnew] == START:
                #     # return paths[y][x]+dnew
                #     ...
                if visited[ynew][xnew]:
                    forward = paths[y][x]

                    backward = pathsInv[y][x]+dnew
                    backward = backward[::-1]
                    backward = backward\
                        .replace('U','u')\
                        .replace('R','r')\
                        .replace('D','d')\
                        .replace('L','l')\
                        .replace('u','D')\
                        .replace('r','L')\
                        .replace('d','U')\
                        .replace('l','R')\

                    return forward+backward

                visitedInv[ynew][xnew] = True
                pathsInv[ynew][xnew] = pathsInv[y][x]+dnew
                qinv.append((ynew, xnew))

    return False

if env=="local":
    t = time.time()
else:
    t = float('inf')

ans = grid_bfs(grid,*start,*end)

if env=="local":
    print(time.time()-t)

if ans:
    print("YES")
    print(len(ans))
    print(ans)
else:
    print("NO")