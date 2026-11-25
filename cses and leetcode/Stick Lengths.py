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
lengths = [*map(int,inputmethod().split(' '))]
lengths.sort()

cumu = [0]
for x in lengths:
    cumu.append(cumu[-1]+x)

# cumu[i] = sum till arr[i-1]
cost = float('inf')
for i in range(n):
    leftSum = cumu[i+1]
    rightSum = cumu[-1]-cumu[i+1]
    leftLength = i+1
    rightLength = n-i-1

    if i+1<n:
        for x in [lengths[i],lengths[i+1]]:
            cost = min(cost,rightSum-leftSum+x*(leftLength-rightLength))
    else:
        x = lengths[i]
        cost = min(cost,rightSum-leftSum+x*(leftLength-rightLength))

print(cost)