from collections import deque
import time

n = int(input() or 8)

def grid_bfs(n):

    ylen = n
    xlen = n

    grid = grid1000[:n-4][:n-4]

    visitedAll = set()

    dx = [2,1,-2,-1,1,-2,-1,2]
    dy = [1,2,-1,-2,-2,1,2,-1]

    q = [(0,0,0)]
    q = deque(q)


    while q:

        topY, topX, topCount = q.popleft()
        
        if grid[topY][topX] == -1:
            grid[topY][topX] = topCount

        for i in range(len(dx)):
            ynew = topY + dy[i]
            xnew = topX + dx[i]

            if not (0 <= ynew < ylen and 0 <= xnew < xlen):
                continue

            # already exists and already filled
            if ynew<len(grid) and xnew<len(grid[ynew]) and grid[ynew][xnew]!=-1:
                continue

            q.append((ynew, xnew, topCount+1))

    return grid


t = time.time()
grid = grid_bfs(n)
print(time.time()-t)
s = ''
for row in grid:
    s+=str(row)+',\n'

print(s)

# f = open('kmgOut.txt','w')
# f.write(s)
# f.close()