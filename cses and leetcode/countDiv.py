# divCount = dict()

divisorCount = [0]*(10**6+1)
def prep():
    global divisorCount

    for i in range(1,10**6+1):
        for j in range(i,10**6+1,i):
            divisorCount[j] += 1

# fl = open('inp.txt','r')

def inputmethod():
    return input()
    return fl.readline().strip()

prep()
t = int(inputmethod())
for _ in range(t):
    n = int(inputmethod())
    print(divisorCount[n])