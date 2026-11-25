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
arr = [*map(lambda x:x-1,map(int,inputmethod().split(' ')))]
arrxi = []
for i,x in enumerate(arr):
    arrxi.append((x,i))
arrxi.sort()

arrI2arrxiI = dict()
for arrxiI in range(n):
    x,arrI = arrxi[arrxiI]
    arrI2arrxiI[arrI] = arrxiI

round = 1
oldI = -1
for x,i in arrxi:
    if i>oldI:
        oldI = i
    else:
        oldI = i
        round+=1

# print(round) # found correct



ans = []
for _ in range(m):
    a,b = [*map(int,inputmethod().split(' '))]
    i = arrI2arrxiI[a-1]
    j = arrI2arrxiI[b-1]

    if abs(i-j)>1:
        previous = 0
        if i+1<n and arrxi[i][1]>arrxi[i+1][1]:
            previous+=1
        if i-1>=0 and arrxi[i-1][1]>arrxi[i][1]:
            previous+=1

        if j+1<n and arrxi[j][1]>arrxi[j+1][1]:
            previous+=1
        if j-1>=0 and arrxi[j-1][1]>arrxi[j][1]:
            previous+=1

        eleI = arrxi[i]
        eleJ = arrxi[j]

        arrxi[j] = (eleJ[0],eleI[1])
        arrxi[i] = (eleI[0],eleJ[1])

        later = 0
        if i+1<n and arrxi[i][1]>arrxi[i+1][1]:
            later+=1
        if i-1>=0 and arrxi[i-1][1]>arrxi[i][1]:
            later+=1

        if j+1<n and arrxi[j][1]>arrxi[j+1][1]:
            later+=1
        if j-1>=0 and arrxi[j-1][1]>arrxi[j][1]:
            later+=1

        round+=later-previous
    elif i==j:
        pass
    else:
        i,j = min(i,j),max(i,j)
        assert j==i+1
        previous = 0
        if i-1>=0 and arrxi[i-1][1]>arrxi[i][1]:
            previous+=1
        if arrxi[i][1]>arrxi[i+1][1]:
            previous+=1
        if i+2<n and arrxi[i+1][1]>arrxi[i+2][1]:
            previous+=1

        eleI = arrxi[i]
        eleJ = arrxi[j]

        arrxi[i] = (eleI[0],eleJ[1])
        arrxi[j] = (eleJ[0],eleI[1])

        later = 0
        if i-1>=0 and arrxi[i-1][1]>arrxi[i][1]:
            later+=1
        if arrxi[i][1]>arrxi[i+1][1]:
            later+=1
        if i+2<n and arrxi[i+1][1]>arrxi[i+2][1]:
            later+=1

        round+=later-previous

    ans.append(str(round))

print(' '.join(ans))