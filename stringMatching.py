try:
    open("__localsystemflag__").close()
    f = open('inp.txt')
    env = 'local'
except FileNotFoundError:
    f = None
    env = 'server'

def inputmethod():
    if f:
        return f.readline().strip()
    else:
        return input()


s = inputmethod()
pattern = inputmethod()

if len(pattern)>len(s):
    print(0)
    exit()
elif len(pattern)==len(s) and pattern==s:
    print(1)
    exit()

# i = -1
# count = 0
# while(True):
#     try:
#         i = s.index(pattern,i+1)
#     except:
#         break
#     count+=1
# print(count)
# exit()

hs = 0
multiplier = 1
num = 71
M = 10**9+7
for p in pattern:
    i = ord(p)
    hs+=i*multiplier
    multiplier*=num

    multiplier%=M
    hs%=M
    # print(hs,p)

hss = 0
multiplier = 1
M = 10**9+7
for j in range(len(pattern)):
    hss+=ord(s[j])*multiplier
    multiplier*=num
    
    multiplier%=M
    hss%=M
    # print(hss,s[j])


inv = pow(num,-1,M)
multiplier*=inv
multiplier%=M

count = 0
if hss==hs:
    # print(s[0:])
    count+=1


for r in range(len(pattern),len(s)):
    hss-=ord(s[r-len(pattern)])
    hss+=M
    hss*=inv
    hss+=(ord(s[r])*multiplier)%M
    hss%=M

    if hss==hs:
        # print(s[i-1:])
        count+=1

    # print(hss,s[i:])

print(count)