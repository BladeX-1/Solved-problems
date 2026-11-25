try:
    f = open('inp.txt')
    env = 'local'
except Exception as e:
    f = None
    env = 'server'

def inputmethod():
    if f:
        return f.readline().strip()
    else:
        return input()

s = inputmethod()
n = len(s)
counter = [0]*26
for c in s:
    counter[ord(c)-ord('A')]+=1

assert sum(counter)==n

ans = []
print(counter)
i = 0
while(i<n):
    failed = True
    for j in range(26):
        if i!=0 and ans[-1]==j:
            continue
        if counter[j]:
            failed = False
            ans.append(j)
            counter[j]-=1
            break
    if failed:
        
        break

    i+=1


print(n,len(ans))
if len(ans)==n:
    print(''.join(map(lambda x:chr(x+ord('A')),ans)))
else:
    print(-1)