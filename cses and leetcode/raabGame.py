f = open('inp.txt')

def inputmethod():
    return f.readline().strip()

t = int(input())
for _ in range(t):
    n,a,b = [*map(int,input().split(' '))]
    if a+b>n:
        print('NO')
        continue
    
    draws = n-a-b

    ans = []

    for i in range(n,n-draws,-1):
        ans.append(i)

    n = a+b
    draws = 0


