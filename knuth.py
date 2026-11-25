# f = open('inp.txt','r')

def inputmethod():
    return input()
    return f.readline().strip()

n = int(inputmethod())
arr = [*map(int,inputmethod().split(' '))]

memo = dict()
def costdp(arr,l,r,cumu):
    if (l,r) in memo:
        return memo[l,r]
    
    if l==r:
        return 0
    
    # starting point of right side
    subans = float('inf')
    for i in range(l+1,r+1):
        subans = min(subans, costdp(arr,l,i-1,cumu) + costdp(arr,i,r,cumu))

    ans = subans + (cumu[r+1]-cumu[l-1+1])
    memo[l,r] = ans
    return ans


cumu = [0]
for x in arr:
    cumu.append(cumu[-1]+x)
    # assert cumu[-1]>cumu[-2]
# cumu[i] = sum till arr[i-1]
# sum till arr[i] = cumu[i+1]

ans = costdp(arr,0,len(arr)-1,cumu)
print(ans)