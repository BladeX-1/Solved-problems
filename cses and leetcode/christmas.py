import math

# f = open("inp.txt",'r')
def inputmethod():
    return input()
    return f.readline().strip()

n = int(inputmethod())

M = 10**9+7


ans = 1
i = 0
for i in range(1,n+1):
    ans = (ans*i+(-1)**i)%M

print(ans)