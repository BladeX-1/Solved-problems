import sys
inputI = -1
inputArr = []
try:
    open("__localsystemflag__").close()
    f = open('inp.txt')
    env = 'local'
except FileNotFoundError:
    inputArr = sys.stdin.read().split('\n')
    inputI = 0
    f = None
    env = 'server'

def inputmethod():
    global inputI
    if f:
        return f.readline().strip()
    else:
        inputI+=1
        return inputArr[inputI-1]
        return input()



n,capacity = [*map(int,inputmethod().split(' '))]
weights = [*map(int,inputmethod().split(' '))]

weights.sort(reverse=True)
rightCumulative = [0]
for i in reversed(range(n)):
    rightCumulative.append(rightCumulative[-1]+weights[i])
rightCumulative.reverse()

# try greedy filling
bucket = 0
count = 1
for i in range(n):
    if bucket+weights[i]<=capacity:
        bucket+=weights[i]
    else:
        count+=1
        bucket = weights[i]
bestAns = count

allOnes = (1<<n)-1
memo = set()
def fillRound(includedBitmask,start,capacityLeft,accum):
    if (includedBitmask,capacityLeft) in memo:
        return

    memo.add((includedBitmask,capacityLeft))
    
    if includedBitmask==allOnes: # all done
        accum.add(includedBitmask)
        return

    for i in reversed(range(n)):
        if includedBitmask&(1<<i):
            continue
        elif capacityLeft<weights[i]: # capacity smaller than smallest weight
            accum.add(includedBitmask)
            return
        else:
            break

    if start==n: ## can fill more, but reached end
        return

    for i in range(start,n):
        if includedBitmask&(1<<i):
            continue
        if weights[i]>capacityLeft:
            continue
        if i!=start and weights[start] == weights[i]:
            continue
        
        fillRound(includedBitmask|(1<<i),i+1,capacityLeft-weights[i],accum)
        if allOnes in accum:
            return accum
    return

def f():
    round = 0
    newAns = set([0])

    while(allOnes not in newAns):
        ans = newAns
        newAns = set()
        round += 1

        assert ans
        
        for a in ans:
            tempx = a
            start = 0
            while(tempx&1):
                tempx>>=1
                start+=1
            temp = set()
            fillRound(a|(1<<start),start+1,capacity-weights[start],temp)
            if allOnes in temp:
                return round
            newAns.update(temp)
        print(newAns)
    assert False


ans = f()
print(ans)