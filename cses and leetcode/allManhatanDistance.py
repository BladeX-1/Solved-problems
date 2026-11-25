# fl = open('inp.txt','r')

def inputmethod():
    return input()
    # return fl.readline().strip()


n = int(inputmethod())
xs = []
ys = []
for _ in range(n):
    x,y = [*map(int,inputmethod().split(' '))]
    xs.append(x)
    ys.append(y)

xs.sort(reverse=True)
ys.sort(reverse=True)

backX = 0
backY = 0
frontY = 0
frontX = 0
for i in range(1,n):
    backX+=xs[i]*i
    backY+=ys[i]*i

    frontX+=xs[i-1]*(n-i)
    frontY+=ys[i-1]*(n-i)

print(frontX+frontY-backX-backY)