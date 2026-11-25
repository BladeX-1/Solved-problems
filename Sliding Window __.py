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

class Window:
    def __init__(self,k):
        self.k = k
        self.counts = dict()
        self.distinctCount = 0

    def add(self,x):
        if x in self.counts:
            self.counts[x] += 1
        else:
            self.counts[x] = 1
            self.distinctCount += 1

    def remove(self,x):
        if x in self.counts:
            self.counts[x] -= 1
            if self.counts[x] == 0:
                del self.counts[x]
                self.distinctCount -= 1

    def getDistinctCount(self):
        return self.distinctCount


window = Window(k)
for i in range(k):
    window.add(arr[i])

ans = [window.getDistinctCount()]
for i in range(k,n):
    window.remove(arr[i-k])
    window.add(arr[i])
    ans.append(window.getDistinctCount())

print(*ans)