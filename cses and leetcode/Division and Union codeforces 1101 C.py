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



t = int(inputmethod())
for _t in range(t):
    n = int(inputmethod())
    segments = []
    for _n in range(n):
        l,r = [*map(int,inputmethod().split())]
        segments.append([l,r,_n])
    segments.sort()

    l,r,_ = segments[0]
    count = 1
    group = [-1]*n
    group[0] = 1
    possible = True
    for i in range(1,n):
        l2,r2,_ = segments[i]
        if r<l2 or r2<l:
            count += 1
            # if count==3:
            #     possible = False
            #     break
            group[i] = count
            l = l2
            r = r2

        else:
            # l = min(l,l2)
            r = max(r,r2)
            group[i] = count

    if count==1:
        print(-1)
    else:
        for i in range(n):
            if group[i]>2:
                group[i]=2
        ans = [-1]*n
        for i in range(n):
            j = segments[i][2]
            ans[j] = group[i]

        ansStr = map(str,ans)
        print(' '.join(ansStr))