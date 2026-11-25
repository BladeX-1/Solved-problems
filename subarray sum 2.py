
def inputmethod():
    return input()


n,target = map(int,inputmethod().split(' '))
arr = map(int,inputmethod().split(' '))

var = 0

mask = 983482374

cumudict = dict()
cumudict[0^mask] = 1
count = 0


for x in arr:
    var += x
    count+=cumudict.get((var-target)^mask,0)
    cumudict[var^mask] = cumudict.get(var^mask,0)+1
print(count)