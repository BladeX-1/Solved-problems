try:
    f = open('inp.txt')
    env = 'local'
except Exception as e:
    f = None
    env = 'server'

def inputmethod():
    if f:
        return f.readline().strip()
    else:
        return input()


n = int(input())
arr = [*map(int,input().split(' '))]
