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



n,m = [*map(int,inputmethod().split(' '))]
mat = []
M = 10**9+7
for _ in range(n):
    coeffs = [*map(int,inputmethod().split(' '))]
    mat.append(coeffs)

xMaster = 0
for yMaster in range(min(n,m)):
    coeff = mat[yMaster][xMaster]
    if coeff == 0:
        for y in range(yMaster+1,n):
            if mat[y][xMaster]!=0:
                for x in range(xMaster,m+1):
                    mat[yMaster][x],mat[y][x] = mat[y][x],mat[yMaster][x]
                break
        coeffs = mat[yMaster][xMaster]
        if coeffs==0:
            xMaster+=1
            continue

    inv = pow(coeff,-1,M)
    for x in range(xMaster,m+1):
        mat[yMaster][x]*=inv
        mat[yMaster][x]%=M

    for y in range(n):
        if y==yMaster:
            continue
        multiplier = mat[y][xMaster]
        for x in range(xMaster,m+1):
            mat[y][x] -= mat[yMaster][x]*multiplier
            mat[y][x] %= M

    xMaster+=1

extraAns = [0]*m
if m>n:
    for i in range(n):
        if mat[i][i]!=0:
            continue

        for x in range(i+1,m):
            if mat[i][x]==0:
                continue
            inv = pow(mat[i][x],-1,M)
            multiplier = mat[i][-1]*inv
            extraAns[x] += multiplier
            extraAns[x] %= M
            for y in range(n):
                mat[y][-1] -= mat[y][x]*multiplier
                mat[y][-1] %= M
            break

ans = []
# for row in mat:
#     print(row)

for y in range(min(m,n)):
    if mat[y][y] != 0 or mat[y][-1]==0:
        ans.append(str(mat[y][-1]))
    else:
        print(-1)
        # print("L 67")
        exit()

if n>m:# height > width
    for y in range(m,n):# enters when n>m
        if mat[y][-1]!=0: # should be zero for solution to exist
            print(-1)
            # print("L 73")
            exit()

if m>n: # width > height
    ans.extend([str(0)]*(m-n))

for x in range(len(extraAns)):
    if extraAns[x] != 0:
        ans[x] = str(extraAns[x])


print(' '.join(ans))