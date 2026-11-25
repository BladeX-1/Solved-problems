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


k = int(inputmethod())

board = [[1]*8 for _ in range(8)]
dy = [0,1,0,-1]
dx = [1,0,-1,0]

def transition(board):
    newBoard = [[0]*8 for _ in range(8)]

    for y in range(8):
        for x in range(8):
            for i in range(4):
                ynew = y+dy[i]
                xnew = x+dx[i]
                if 0<=ynew<8 and 0<=xnew<8:
                    newBoard[ynew][xnew] += board[y][x]/4

    return newBoard

for _ in range(k):
    board = transition(board)

# for y in range(8):
#     for x in range(8):

sum_ = 64-sum_
print(round(sum_,6))