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



ylen,xlen = [*map(int,inputmethod().split())]
start = [-1,-1]
end = [-1,-1]
grid = []
for y in range(ylen):
    row = inputmethod()
    grid.append(row)
    if start[0]==-1 and 'S' in row:
        start = [y,row.index('S')]
    if end[0]==-1 and 'T' in row:
        end = [y,row.index('T')]

import heapq
def grid_bfs(grid, start):
    # def bfs_grid(grid,y,x):

    ylen = len(grid)
    xlen = len(grid[0])

    # visited = set()

    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    dd = "DRUL"
    visited = dict()

    # def isBounded(y_,x_,ylen,xlen):
    def isBounded(y_, x_):
        return 0 <= y_ < ylen and 0 <= x_ < xlen

    q = [[0,'',0,start[0],start[1]]]
    while q:
        topCost, topDir, topDirLen, topY, topX = heapq.heappop(q)
        if grid[topY][topX]=='T':
            return topCost
        if (topY,topX) in visited and visited[(topY,topX)]<topCost:
            continue
        for i in range(4):
            ynew = topY + dy[i]
            xnew = topX + dx[i]
            dnew = dd[i]

            if not isBounded(ynew, xnew):
                continue
            if grid[ynew][xnew]=='#':
                continue
            if topDir==dnew:
                if topDirLen+1>3:
                    if (ynew,xnew) not in visited or visited[(ynew,xnew)]>topCost+3:
                        visited[(ynew,xnew)] = topCost+3
                        heapq.heappush(q,([topCost+3,dnew,2,ynew,xnew]))
                else:
                    if (ynew,xnew) not in visited or visited[(ynew,xnew)]>topCost+1:
                        visited[(ynew,xnew)] = topCost+1
                        heapq.heappush(q,([topCost+1,dnew,topDirLen+1,ynew,xnew]))
            else:
                if (ynew, xnew) not in visited or visited[(ynew, xnew)]>topCost+1:
                    visited[(ynew, xnew)] = topCost+1
                    heapq.heappush(q,([topCost+1,dnew,1,ynew, xnew]))
    return -1


ans = grid_bfs(grid,start)
print(ans)