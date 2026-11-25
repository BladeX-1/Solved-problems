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

n,k = [*map(int,inputmethod().split(' '))]
arr = [*map(int,inputmethod().split(' '))]

low = max(max(arr),sum(arr)//k)
high = min(sum(arr),(max(arr)*n)//k)

def fillElements(arr,maximum,k):
    bucket = 0
    currentFilling = 1
    for i in range(len(arr)):
        if bucket+arr[i]>maximum:
            bucket = 0
            currentFilling += 1
            if currentFilling>k:
                return False
        bucket+=arr[i]

    return True

ans = high
while(low<=igh):
    mid = (low+high)//2
    isFilled = fillElements(arr,mid,k)
    if not isFilled:
        low = mid+1
    else:
        ans = mid
        high = mid-1

print(ans)