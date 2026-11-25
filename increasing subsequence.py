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


n = int(inputmethod())
arr = [*map(int,inputmethod().split(' '))]

dp = [1]*n
# dp[i] is lenght of longest subsequence starting from i
for i in reversed(range(n-1)):
    for j in range(i+1,n):
        if arr[i]<arr[j] and dp[i]<dp[j]+1:
            dp[i] = dp[j]+1


mx = max(dp)
print(mx)