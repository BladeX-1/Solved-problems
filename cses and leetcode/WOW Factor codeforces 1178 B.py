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



s = inputmethod()
n = len(s)
compressed = []
l = -1
r = -1
for i in range(n):
    if i==0 or s[i-1]!=s[i]:
        l = i

    if i==n-1 or s[i]!=s[i+1]:
        r = i
        c = s[i]
        if c=='v':
            if r-l+1-1>0:
                compressed.append(['w',r-l+1-1])
        elif c=='o':
            compressed.append(['o',r-l+1])

for i in reversed(range(1,len(compressed))):
    if compressed[i-1][0]==compressed[i]:
        compressed[i-1][1]+=compressed[i][1]
        compressed[i] = []

compressed2 = []
for i in range(len(compressed)):
    if compressed[i]!=[]:
        compressed2.append(compressed[i])

wOnLeft = [0]
for i in range(len(compressed2)):
    if compressed2[i][0]=='w':
        wOnLeft.append(wOnLeft[-1]+compressed2[i][1])
    else:
        wOnLeft.append(wOnLeft[-1])
wOnLeft.pop(-1)


wOnRight = [0]
for i in reversed(range(len(compressed2))):
    if compressed2[i][0]=='w':
        wOnRight.append(wOnRight[-1]+compressed2[i][1])
    else:
        wOnRight.append(wOnRight[-1])

wOnRight.pop(-1)
wOnRight.reverse()

ans = 0
for i in range(len(compressed2)):
    if compressed2[i][0]=='o':
        ans+=wOnLeft[i]*compressed2[i][1]*wOnRight[i]

print(ans)