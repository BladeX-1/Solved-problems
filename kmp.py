s = 'askfwenlasabcajls'
pat = 'abcac'

moveOnMismatch = [0]*len(pat)
l = 0
for i in range(1,len(pat)):
    if pat[l]==pat[i]:
        l+=1
        moveOnMismatch[i] = l
    else:
        l=0
        moveOnMismatch[i] = l

print(moveOnMismatch)

si = 0
pi = 0
while(pi<len(pat) and si<len(s)):
    if pat[pi]==s[si]:
        si+=1
        pi+=1
    else:
        if pi!=0:
            pi = moveOnMismatch[pi-1]
        else:
            si+=1

    if pi==len(pat):
        print('found')
    