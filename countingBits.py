n = int(input())
flag = 1
ans = 0
while(flag//2<=n):
    if flag==1:
        ans+=(n+1)//2
        flag *= 2
        continue

    # k*2**x+h, k = flag//2
    ans += max(0,n%(2*flag)-flag+1)+2*n&(2*flag)
    flag*=2

print(ans)