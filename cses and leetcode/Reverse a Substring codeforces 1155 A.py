import sys
inputI_23235231253 = -1
inputArr_6273468273 = []
try:
    open("__localsystemflag__").close()
    file_input_txt_2342349 = open('inp.txt')
    env = 'local'
except FileNotFoundError:
    rawInput_568279834 = sys.stdin.read()
    inputArr_6273468273 = rawInput_568279834.splitlines()
    
    inputI_23235231253 = 0
    file_input_txt_2342349 = None
    env = 'server'

def inputmethod():
    global inputI_23235231253
    if file_input_txt_2342349:
        return file_input_txt_2342349.readline().strip()
    else:
        inputI_23235231253+=1
        return inputArr_6273468273[inputI_23235231253-1]
        return input()



n = int(inputmethod())
s = list(inputmethod())

sSorted = s[:]
sSorted.sort()

r = -1
for i in reversed(range(n)):
    if sSorted[i]==s[i]:
        continue
    else:
        r = i
        break

if r==-1:
    print("NO")
else:

    l = -1
    for i in range(0,r):
        if s[i]>s[r]:
            l = i
            break

    # newS = s[:l]+s[l:r+1][::-1]+s[r+1:]
    print("YES")
    print(l+1,r+1)
    # print(''.join(newS))