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

    

n,m = [*map(int,input().split(' '))]

arr = [*map(int,input().split(' '))]

M = 10**9+7

l = 0
ans = 1
while(l<n):
    temp = 0
    if arr[l] == 0 and (l==0 or arr[l-1]!=0): # capture first zero
        for r in range(l,n):
            if r==n-1 or arr[r+1]!=0: # capture last zero
                zeroCount = r-l+1
                assert l!=0 or r!=n-1, "l and r cannot be both at the edge"
                if (l==0 or r==n-1): # if one is at the edge
                    temp+=pow(3,zeroCount,M)
                    break
                else:
                    ...
        ans = (ans*temp)%M
    l+=1