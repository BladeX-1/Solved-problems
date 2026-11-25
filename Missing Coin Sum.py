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



n = int(inputmethod())
coins = [*map(int,inputmethod().split(' '))]
coins.sort()

target = 1
for i in range(n):
    if coins[i]>target:
        print(target)
        exit()
    else:
        target+=coins[i]

print(target)