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
readingTime = [*map(int,inputmethod().split(' '))]
readingTime.sort()

sum_ = sum(readingTime)
if sum_-readingTime[-1]<=readingTime[-1]:
    print(2*readingTime[-1])
else:
    print(sum_)