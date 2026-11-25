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
cubes = [*map(int,inputmethod().split(' '))]

towers = []
import bisect
for c in cubes:
    if not towers:
        towers.append(c)
        continue

    i = bisect.bisect_right(towers,c)
    if i==len(towers):
        towers.append(c)
    else:
        towers[i] = c

print(len(towers))