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
arr2 = []
for i in range(n):
    arr2.append((arr[i],i))

arr2.sort()
rounds = 1
ind = 0
for i in range(n):
    x,j = arr2[i]
    if j<ind:
        rounds+=1
        ind = j
    else:
        ind = j

print(rounds)