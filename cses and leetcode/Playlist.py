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

window = set()
l=0
ans = 0
for r in range(n):
    if arr[r] in window:
        while(arr[l]!=arr[r]):
            window.remove(arr[l])
            l+=1
        window.remove(arr[l])
        l+=1
    window.add(arr[r])
    ans = max(ans,len(window))

print(ans)