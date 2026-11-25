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



ylen,xlen = [*map(int,inputmethod().split(' '))]
grid = []
ystart = None
xstart = None
monsters = []
for y_ in range(ylen):
    row = inputmethod()
    if not ystart and 'A' in row:
        ystart = y_
        xstart = row.index('A')

    i = 0
    try:
        while(True):
            j = row.index('M',i)
            monsters.append((y_,j))
            i = j+1
    except:
        pass
    grid.append(row)

# print("initial of A",y,x)
if ystart in [0,ylen-1] or xstart in [0,xlen-1]:
    print("YES")
    print(0)
    exit()
empty = 0
EMPTY = '.'
for y in range(ylen):
    if grid[y][0]==EMPTY or grid[y][-1]==EMPTY:
        empty += 1
        break
if not empty:
    for x in range(xlen):
        if grid[0][x]==EMPTY or grid[-1][x]==EMPTY:
            empty += 1
            break

if empty==0:
    print('NO')
    exit()

WALL = '#'
def grid_bfs(grid, y, x, monsters):
    # def bfs_grid(grid,y,x):

    ylen = len(grid)
    xlen = len(grid[0])

    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]



    # def isBounded(y_,x_,ylen,xlen):
    def isBounded(y_, x_):
        return 0 <= y_ < ylen and 0 <= x_ < xlen

    def isAtEdge(y_,x_):
        return (y_==0 or y_==ylen-1) or (x_==0 or x_==xlen-1)

    ###  y,x (parentY,parentX)
    q = [(y, x, (-1,-1)),(None,None,(None,None))]
    qMonster = monsters+[(None,None)]
    visited = set()
    visited.add((y,x))
    visitedmonsters = set(monsters)
    parents = dict()
    found = False
    qNone = (None,None,(None,None))
    qMonsterNone = (None,None)
    yend = None
    xend = None
    while len(q)>1:
        while len(q)>1:
            topY, topX, topParent = q.pop(0)
            if topY == None:
                # process all of single layer, then break
                q.append(qNone)
                break

            # skip if monster already reached there
            if (topY,topX) in visitedmonsters:
                continue

            if topParent[0]!=-1:
                parents[(topY,topX)] = topParent
            
            for i in range(4):
                ynew = topY + dy[i]
                xnew = topX + dx[i]

                if not isBounded(ynew, xnew):
                    # parents[(ynew,xnew)] = (topY,topX)
                    found = True
                    yend = topY
                    xend = topX
                    break
                if (ynew, xnew) in visited:
                    continue
                if grid[ynew][xnew] == WALL:
                    continue
                if (ynew,xnew) in visitedmonsters: # skip the cells where a monster could be
                    continue

                visited.add((ynew, xnew))
                q.append((ynew, xnew, (topY,topX)))

            if found:
                break
        if found:
            break

        while len(qMonster)>1:
            monsterTopY, monsterTopX = qMonster.pop(0)
            if monsterTopY==None:
                qMonster.append(qMonsterNone)
                break

            for i in range(4):
                ynew = monsterTopY + dy[i]
                xnew = monsterTopX + dx[i]

                if not isBounded(ynew, xnew):
                    continue
                if (ynew, xnew) in visitedmonsters:
                    continue
                if grid[ynew][xnew] == WALL:
                    continue
                    

                visitedmonsters.add((ynew, xnew))
                qMonster.append((ynew, xnew))

    if not found:
        print('NO')
        return
    else:
        print("YES")
        ans = []
        # yend,xend,parents
        y = yend
        x = xend
        ans.append((y,x))
        while((y,x) in parents):
            y,x = parents[(y,x)]
            ans.append((y,x))

        ans.reverse()

        ansDirections = []
        directionArr = [(1,0),(-1,0),(0,1),(0,-1)]
        dir = "DURL"
        for i in range(len(ans)-1):
            left = ans[i]
            right = ans[i+1]
            dely = right[0]-left[0]
            delx = right[1]-left[1]

            d = dir[directionArr.index((dely,delx))]
            ansDirections.append(d)

        print(len(ansDirections))
        print(*ansDirections,sep='')



grid_bfs(grid,ystart,xstart,monsters)