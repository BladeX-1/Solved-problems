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



s = inputmethod()
n = len(s)


M = 10**9+7
bases = [37,31]
answer = set()
orda = ord('a')
for enm,base in enumerate(bases):
    basePower = 1
    frontHash = 0
    backHash = 0
    answertemp = set()
    for i in range(n-1):
        frontHash += basePower*(ord(s[i])-orda)
        frontHash%=M

        backHash *= base
        backHash+=(ord(s[n-1-i])-orda)
        backHash%=M

        if frontHash==backHash:
            # print(i+1)
            answertemp.add(i+1)

        basePower*= base
        basePower%=M

    if enm != 0:
        answer = answer.intersection(answertemp)
    else:
        answer = answertemp





print(' '.join(map(str,sorted(answer))))