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



n,k = [*map(int,inputmethod().split(' '))]
numbers = []
for _ in range(n):
    s = inputmethod()
    i = int(s,base=2)
    numbers.append(i)

ans = k
for i in range(n):
    for j in range(i+1,n):
        temp = (numbers[i]^numbers[j]).bit_count()
        if temp<ans:
            ans=temp

print(ans)