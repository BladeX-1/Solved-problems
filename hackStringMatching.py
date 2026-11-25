M = 10**9+7
B = 990
pattern = 'aaaaaa'
s = 'zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz'

b = 1
patternHash = 0
for c in reversed(pattern):
    i = ord(c)-ord('a')+1
    patternHash += (i*b)%M
    patternHash %= M
    b*=B
    b%=M
print(patternHash)

b=1
sHash = 0
for i in reversed(range(len(pattern))):
    j = ord(s[i])-ord('a')+1
    sHash += (j*b)%M
    sHash %= M
    b *= B
    b %= M

print(sHash)
if patternHash == sHash:
    print('here startL', s[0:])
for r in range(len(pattern),len(s)):
    sHash*=B
    sHash-=(ord(s[r-len(pattern)])-ord('a')+1)*pow(B,len(pattern),M)
    sHash+=ord(s[r])-ord('a')+1+M
    sHash%=M

    if patternHash==sHash:
        print('there end:',s[:r+1])

