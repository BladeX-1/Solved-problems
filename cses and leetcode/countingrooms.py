def grid_bfs(grid, y, x, visited):
    # def bfs_grid(grid,y,x):

    ylen = len(grid)
    xlen = len(grid[0])

    # visited = set()

    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]

    # def isBounded(y_,x_,ylen,xlen):
    def isBounded(y_, x_):
        return 0 <= y_ < ylen and 0 <= x_ < xlen

    q = [(y, x)]
    while q:
        topY, topX = q.pop(0)

        for i in range(4):
            ynew = topY + dy[i]
            xnew = topX + dx[i]

            if not isBounded(ynew, xnew):
                continue
            if visited[ynew][xnew]:
                continue
            if grid[ynew][xnew] == WALL_INT:
                continue

            visited[ynew][xnew] = True
            q.append((ynew, xnew))

WALL = '#'
ROOM = '.'
WALL_INT = 0
ROOM_INT = 1


# f = open("countingroomsInput.txt", "r")
def inputmethod():
    return input()
    # return f.readline().strip()

ylen, xlen = [*map(int,inputmethod().split(' '))]
grid = []
for y in range(ylen):
    grid.append([*map(lambda x: int(x == ROOM), list(inputmethod()))])

assert len(grid) == ylen
assert len(grid[0]) == xlen

visited = [[False] * xlen for _ in range(ylen)]
roomCount = 0
for y in range(ylen):
    for x in range(xlen):
        if grid[y][x] == WALL_INT:
            continue
        if visited[y][x]:
            continue

        visited[y][x] = True
        roomCount += 1
        grid_bfs(grid, y, x, visited)

print(roomCount)