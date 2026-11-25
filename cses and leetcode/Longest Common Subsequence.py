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



a,b = [*map(int,inputmethod().split(' '))]
arr = [*map(int,inputmethod().split(' '))]
brr = [*map(int,inputmethod().split(' '))]

def lcs(ai,bi,memo):
    if ai==a or bi==b:
        return 0,[]

    if (ai,bi) in memo:
        return memo[ai,bi]

    if arr[ai]==brr[bi]:
        nextlength,nextsubsequence = lcs(ai+1,bi+1,memo)
        ans = nextlength+1,[arr[ai]]+nextsubsequence

    else:
        nextlength1,nextsubsequence1 = lcs(ai+1,bi,memo)
        nextlength2,nextsubsequence2 = lcs(ai,bi+1,memo)

        if nextlength1>=nextlength2:
            ans = nextlength1,nextsubsequence1
        else:
            ans = nextlength2,nextsubsequence2

    memo[ai,bi] = ans
    return ans

# length,subsequence = lcs(0,0,dict())
# print(length)
# print(*subsequence)

from collections import Counter
ca = Counter(arr)
cb = Counter(arr)

if len(ca.keys())==len(cb.keys())==1 \
    and arr[0]==brr[0]:
    if a<b:
        print(a)
        print(*arr)
    else:
        print(b)
        print(*brr)
    exit()

if len(set(arr)&set(brr))==0:
    print(0)
    exit()


common = (ca&cb)
maxCommon = 0
for k,v in common.items():
    maxCommon+=v

if maxCommon==1:
    print(1)
    for k,v in common.items():
        print(k)
        exit()

dp = [[0]*(b+1) for _ in range((a+1))]
dpseq = [[[] for _ in range((b+1))] for _ in range((a+1))]

for ai in reversed(range(a)):
    for bi in reversed(range(b)):
        if arr[ai]==brr[bi]:
            dp[ai][bi] = dp[ai+1][bi+1]+1
            dpseq[ai][bi] = [arr[ai]]+dpseq[ai+1][bi+1]
            if dp[ai][bi]==maxCommon:
                print(maxCommon)
                print(*dpseq[ai][bi])
                exit()
        else:
            if dp[ai+1][bi]>=dp[ai][bi+1]:
                dp[ai][bi] = dp[ai+1][bi]
                dpseq[ai][bi] = dpseq[ai+1][bi]
            else:
                dp[ai][bi] = dp[ai][bi+1]
                dpseq[ai][bi] = dpseq[ai][bi+1]


length = dp[0][0]
subsequence = dpseq[0][0]
print(length)

print(' '.join(map(str,subsequence)))