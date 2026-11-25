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

import math

t = int(inputmethod())
for _ in range(t):
    p = int(inputmethod())

    if p==1 or p==0:
        print(2)
        continue
    if p == 2:
        print(3)
        continue

    if p%2==0:
        p-=1
        
    p+=2
    # p is odd

    ans = None
    while(not ans):
        found = True
        for i in range(3,math.ceil(math.sqrt(p))+1,2):
            if p%i==0:
                found = False
                break
        if found:
            ans = p
            break
        p+=2
    print(ans)