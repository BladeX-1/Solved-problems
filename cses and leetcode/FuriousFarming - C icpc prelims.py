import sys
inputI = -1
inputArr = []
spliter = "\n"
try:
    open("__localsystemflag__").close()
    f = open('inp.txt')
    env = 'local'
except FileNotFoundError:
    rawInput = sys.stdin.read()
    inputArr = rawInput.splitlines()
    
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



t = int(inputmethod())
for _ in range(t):
    fieldCount, cloudCount = [*map(int,inputmethod().split())]
    clouds = [*map(int,inputmethod().split())]

    clouds.sort()

    leftEmptyFields = clouds[0]-1
    rightEmptyFields = fieldCount-clouds[-1]

    assert leftEmptyFields>=0
    assert rightEmptyFields>=0

    ans1 = leftEmptyFields + rightEmptyFields + min(leftEmptyFields, rightEmptyFields)

    maxEmpty = 0
    for i in range(cloudCount-1):
        a = clouds[i+1]-leftEmptyFields
        b = clouds[i]+rightEmptyFields
        temp = max(a-1-b,0)

        maxEmpty = max(maxEmpty,temp)

    if maxEmpty==0:
        print(ans1)
        continue
    ans2 = maxEmpty + leftEmptyFields + rightEmptyFields + min(leftEmptyFields+maxEmpty, rightEmptyFields, leftEmptyFields,rightEmptyFields+maxEmpty)

    print(ans2)