def inputmethod():
    return input()
    # return f.readline().strip()

# print(inputmethod())
t = int(inputmethod())
M = 10**9+7
for _ in range(t):
    a,b,c = [*map(int,inputmethod().split(' '))]
    p1 = pow(b,c,M-1)
    p2 = pow(a,p1,M)
    print(p2)