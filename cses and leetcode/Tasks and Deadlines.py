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
arr = []
for _ in range(n):
    duration,deadline = [*map(int,inputmethod().split(' '))]
    arr.append((duration,deadline))

# algo: do the shortest task first, so that there is one less task that do -1 in our rewards
arr.sort()
i=0
reward = 0
for dur,deadline in arr:
    end = i+dur
    reward += deadline-end
    # print(i,end,reward)
    i = end

print(reward)