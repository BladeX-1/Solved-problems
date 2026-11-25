# import subprocess
import time
# s=input()
s = "???R????????L???????????????????????????????????"
# print(f"{len(s)=}")
si=0 #to work on this index on string

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
dz = ['D','R','U','L']



# Clear the Windows screen
def clear_screen():
    pass
    # subprocess.run("cls", shell=True)

def getIslandCount(grid,y,x):
    return -99
    ylen = len(grid)
    xlen = len(grid[0])
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    

    def dfs(grid, y, x, visited):

        def isBounded(y_, x_):
            return 0 <= y_ < ylen and 0 <= x_ < xlen

        for i in range(4):
            ynew = y + dy[i]
            xnew = x + dx[i]

            if not isBounded(ynew, xnew):
                continue
            if (ynew, xnew) in visited:
                continue
            if grid[ynew][xnew]==True:
                continue

            visited.add((ynew, xnew))

            dfs(grid, ynew, xnew, visited)

    visited = set()
    count = 0
    for y in range(ylen):
        for x in range(xlen):
            if (y,x) in visited:
                continue
            if grid[y][x] == True:
                continue

            visited.add((y,x))
            dfs(grid,y,x,visited)
            count+=1

    return count



count = 0
grid = [[False]*7 for _ in range(7)]
grid[0][0] = True

def printGrid(y,x, *args):
    # return
    global grid
    clear_screen()
    if y is not None:
        for i in range(len(grid)):
            row = grid[i]
            rowlist = list(map(lambda b:'X' if b else '-',row))
            if i==y:
                rowlist[x] = '+'
            print(''.join(rowlist))

    print(*args)

def grid_dfs(grid, y, x, s, si):
    global count

    ylen = len(grid)
    xlen = len(grid[0])

    componentCount = getIslandCount(grid,y,x)
    if componentCount>1:
        printGrid(y,x)
        pass


    if True:
        # printGrid(y,x)
        pass
    

    if x==0 and y==6 and si==len(s):
        count+=1
        # printGrid(None,None,count)
        return True
    elif (x==0 and y==6) or si==len(s):
        return False
    

    def isBounded(y_, x_):
        return 0 <= y_ < ylen and 0 <= x_ < xlen

    for i in range(4):
        if s[si]=='?':
            ynew = y + dy[i]
            xnew = x + dx[i]
            d = dz[i]
        else:
            di = dz.index(s[si])
            d = dz[di]
            ynew = y+dy[di]
            xnew = x+dx[di]

        if not isBounded(ynew, xnew):
            continue
        if grid[ynew][xnew]:
            continue

        if d == 'U' \
            and (
                    ( # found the top edge or edge by already path
                        ynew==0\
                        or grid[ynew-1][xnew]
                    ) \
                    and (\
                            xnew==0 \
                            or xnew==6 \
                            or not grid[ynew][xnew-1] and not grid[ynew][xnew+1]\
                    )\
                    
                    or (\
                        ynew>0 and xnew>0 # left-up diagonal be available
                        and grid[ynew-1][xnew-1] # and it is filled already
                        and not grid[ynew][xnew-1] and not grid[ynew-1][xnew] # and both up and left are empty
                    )

                    or (\
                        ynew>0 and xnew!=6 #right-up diagonal be available
                        and grid[ynew-1][xnew+1] # and it is filled already
                        and not grid[ynew][xnew+1] and not grid[ynew-1][xnew] # and both up and right are empty
                    )
            ):
            
                # printGrid(ynew,xnew,'skip',"U")
                continue

        if d == 'D' \
            and (
                    # found the bottom edge or edge by already path
                    (ynew==6 or grid[ynew+1][xnew])
                    and xnew!=0 and xnew!=6
                    and not grid[ynew][xnew-1] and not grid[ynew][xnew+1]\
                    
                    or (\
                        ynew+1<7 and xnew-1>=0 # left-down diagonal be available
                        and grid[ynew+1][xnew-1] # and it is filled already
                        and not grid[ynew+1][xnew] and not grid[ynew][xnew-1] # and both down and left are empty
                    )

                    or (\
                        ynew+1<7 and xnew+1<7 # right-down diagonal be available
                        and grid[ynew+1][xnew+1] # it is filled already
                        and not grid[ynew+1][xnew] and not grid[ynew][xnew+1] # both down and right are empty
                    )
            ):
            
                # printGrid(ynew,xnew,'skip',"D")
                continue

        if d == 'L' \
            and (
                    # found the left edge or edge by already path
                    (
                        xnew == 0 # left edge
                        or grid[ynew][xnew-1] # left block is already filled
                    )
                    and ynew!=0 and ynew!=6 # top and bottom are empty # and they are both empty
                    and not grid[ynew-1][xnew] and not grid[ynew+1][xnew]\
                    
                    or (\
                        ynew-1>=0 and xnew-1>=0 # left-up diagonal be available
                        and grid[ynew-1][xnew-1] # and it is filled already
                        and not grid[ynew-1][xnew] and not grid[ynew][xnew-1] # and both up and left are empty
                    )

                    or (\
                        ynew+1<7 and xnew-1>=0 # left-down diagonal be available
                        and grid[ynew+1][xnew-1] # it is filled already
                        and not grid[ynew+1][xnew] and not grid[ynew][xnew-1] # both down and left are empty
                    )
            ):
                # printGrid(ynew,xnew,'skip',"L")
                continue

        if d == 'R' \
            and (
                    # found the right edge or edge by already path
                    (
                        xnew == 6 # right edge
                        or grid[ynew][xnew+1] # right block is already filled
                    )
                    and ynew!=0 and ynew!=6 # top and bottom are empty # and they are both empty
                    and not grid[ynew-1][xnew] and not grid[ynew+1][xnew]\
                    
                    or (\
                        ynew-1>=0 and xnew+1<7 # right-up diagonal be available
                        and grid[ynew-1][xnew+1] # and it is filled already
                        and not grid[ynew-1][xnew] and not grid[ynew][xnew+1] # and both up and right are empty
                    )

                    or (\
                        ynew+1<7 and xnew+1<7 # right-down diagonal be available
                        and grid[ynew+1][xnew+1] # it is filled already
                        and not grid[ynew+1][xnew] and not grid[ynew][xnew+1] # both down and right are empty
                    )
            ):
                # printGrid(ynew,xnew,'skip',"R")
                continue


        grid[ynew][xnew] = True
        grid_dfs(grid, ynew, xnew, s, si+1)
        grid[ynew][xnew] = False

        if s[si]!='?':
            break

    grid[y][x] = 'x'

t = time.time()
grid_dfs(grid, 0, 0, s, 0)
printGrid(None,None,time.time()-t)
print(count)