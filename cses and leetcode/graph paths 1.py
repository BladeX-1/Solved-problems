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



M = 10**9+7

n,m,k = [*map(int,inputmethod().split(' '))]
mat = [[0]*n for _ in range(n)]
for _ in range(m):
    a,b = [*map(int,inputmethod().split(' '))]
    mat[a-1][b-1] += 1

def matMult(m1,m2):
    m3 = [[0]*n for _ in range(n)]

    for row1 in range(n):
        for col1 in range(n):
            for i in range(n):
                m3[row1][col1] += m1[row1][i]*m2[i][col1]
            m3[row1][col1]%=M

    return m3

def matPower(m,p):
    # returns shallow copy

    if p==1:
        return m

    halfPower = matPower(m,p//2)

    twoHalfPower = matMult(halfPower,halfPower)
    if p%2==1:
        return matMult(twoHalfPower,m)
    else:
        return twoHalfPower


powerk = matPower(mat,k)
print(powerk[0][n-1])