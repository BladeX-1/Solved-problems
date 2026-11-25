import sys

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

machines,products = [*map(int,inputmethod().split(' '))]
times = [*map(int,inputmethod().split(' '))]
# find shortest time
times.sort()
assert len(times)==machines


def getProduce(time):
    produce = 0
    for t in times:
        produce += time//t
        if t>time:
            break
    return produce

ans = float('inf')
minTime = times[0]*(products//machines)
maxTime = times[0]*products
while(minTime<=maxTime):
    mid = (minTime+maxTime)//2
    produce = getProduce(mid)
    if produce<products:
        minTime = mid+1
    else:
        ans = mid
        maxTime = mid-1

print(ans)