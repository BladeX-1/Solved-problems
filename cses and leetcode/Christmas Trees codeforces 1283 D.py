import sys
inputI_23235231253 = -1
inputArr_6273468273 = []
try:
    open("__localsystemflag__").close()
    file_input_txt_2342349 = open('inp.txt')
    env = 'local'
except FileNotFoundError:
    rawInput_568279834 = sys.stdin.read()
    inputArr_6273468273 = rawInput_568279834.splitlines()
    
    inputI_23235231253 = 0
    file_input_txt_2342349 = None
    env = 'server'

def inputmethod():
    global inputI_23235231253
    if file_input_txt_2342349:
        return file_input_txt_2342349.readline().strip()
    else:
        inputI_23235231253+=1
        return inputArr_6273468273[inputI_23235231253-1]
        return input()


from collections import deque
n,people = [*map(int,inputmethod().split())]
trees = [*map(int,inputmethod().split())]
trees.sort()
intervals = deque()
intervals.append([-float('inf'),trees[0]-1,1])
for i in range(0,n-1):
    if trees[i]+1<=trees[i+1]-1:
        intervals.append([trees[i]+1,trees[i+1]-1,1])

intervals.append([trees[-1]+1,float('inf'),1])

inf=float('inf')
positions = []
i = 0
ans = 0
while(i<people):
    l,r,j = intervals.popleft()
    if l==-inf:
        positions.append(r)
        intervals.append([l,r-1,j+1])
        ans+=j
        i+=1
    elif r==inf:
        positions.append(l)
        intervals.append([l+1,r,j+1])
        ans+=j
        i+=1
    elif i+2<=people:
        if l!=r:
            positions.append(l)
            positions.append(r)
            if l+1<=r-1:
                intervals.append([l+1,r-1,j+1])
            ans+=2*j
            i+=2
        elif l==r:
            positions.append(l)
            ans+=j
            i+=1
    elif i+1<=people:
        positions.append(l)
        if l+1<=r:
            intervals.append([l+1,r,None])
        ans+=j
        i+=1
    else:
        assert False

print(ans)
print(*positions)