x,y=map(int,(input().split()))
x-=1
y-=1
 
board=[]
for i in range(8):
    board.append([])
    for j in range(8):
        board[i].append(0)
 
def isbounded(x,y):
    return ((0<=x<=7) and (0<=y<=7))
 
 
def f(i,x,y):
    global board
    board[y][x]=i
    if(i>=64):
        return True #or something
    
    
    dx=[ 2, 1,-1,-2,-2,-1, 1, 2]
    dy=[-1,-2,-2,-1, 1, 2, 2, 1]
    for j in range(8):
        nx,ny=x+dx[j],y+dy[j]
        if((isbounded(nx,ny)) and (board[ny][nx]==0) ):
            flag=f(i+1,nx,ny)
            if(flag):
                return True
    board[y][x]=0
    return False
_=f(1,x,y)
 
 
for y in range(8):
    for x in range(8):
        print(board[y][x],' ',sep='',end='')
    print()