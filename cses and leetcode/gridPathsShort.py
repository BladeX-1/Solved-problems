s=input()
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
dz = ['D','R','U','L']
count = 0
grid = [[False]*7 for _ in range(7)]
grid[0][0] = True
def grid_dfs(grid, y, x, s, si):
 global count
 ylen = len(grid)
 xlen = len(grid[0])
 if x==0 and y==6 and si==len(s):
  count+=1
  return
 elif (x==0 and y==6) or si==len(s):
  return
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
     (
      ynew==0\
      or grid[ynew-1][xnew]
     )\
     and (\
       xnew==0 \
       or xnew==6 \
       or not grid[ynew][xnew-1] and not grid[ynew][xnew+1]\
     )\
     
     or (\
      ynew>0 and xnew>0
      and grid[ynew-1][xnew-1]
      and not grid[ynew][xnew-1] and not grid[ynew-1][xnew]
     )

     or (\
      ynew>0 and xnew!=6
      and grid[ynew-1][xnew+1]
      and not grid[ynew][xnew+1] and not grid[ynew-1][xnew]
     )
   ):
    continue
  if d == 'D' \
   and (
     (ynew==6 or grid[ynew+1][xnew])
     and xnew!=0 and xnew!=6
     and not grid[ynew][xnew-1] and not grid[ynew][xnew+1]\
     
     or (\
      ynew+1<7 and xnew-1>=0
      and grid[ynew+1][xnew-1]
      and not grid[ynew+1][xnew] and not grid[ynew][xnew-1]
     )

     or (\
      ynew+1<7 and xnew+1<7
      and grid[ynew+1][xnew+1]
      and not grid[ynew+1][xnew] and not grid[ynew][xnew+1]
     )
   ):
    continue
  if d == 'L' \
   and (
     (
      xnew == 0
      or grid[ynew][xnew-1]
     )
     and ynew!=0 and ynew!=6
     and not grid[ynew-1][xnew] and not grid[ynew+1][xnew]\
     or (\
      ynew-1>=0 and xnew-1>=0
      and grid[ynew-1][xnew-1]
      and not grid[ynew-1][xnew] and not grid[ynew][xnew-1]
     )
     or (\
      ynew+1<7 and xnew-1>=0
      and grid[ynew+1][xnew-1]
      and not grid[ynew+1][xnew] and not grid[ynew][xnew-1]
     )
   ):
    continue
  if d == 'R' \
   and (
     (
      xnew == 6
      or grid[ynew][xnew+1]
     )
     and ynew!=0 and ynew!=6
     and not grid[ynew-1][xnew] and not grid[ynew+1][xnew]\
     or (\
      ynew-1>=0 and xnew+1<7
      and grid[ynew-1][xnew+1]
      and not grid[ynew-1][xnew] and not grid[ynew][xnew+1]
     )
     or (\
      ynew+1<7 and xnew+1<7
      and grid[ynew+1][xnew+1]
      and not grid[ynew+1][xnew] and not grid[ynew][xnew+1]
     )
   ):
    continue
  grid[ynew][xnew] = True
  grid_dfs(grid, ynew, xnew, s, si+1)
  grid[ynew][xnew] = False
  if s[si]!='?':
   break
 grid[y][x] = 'x'

grid_dfs(grid, 0, 0, s, 0)
print(count)