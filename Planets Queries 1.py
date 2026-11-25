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


    

n, q = [*map(int,inputmethod().split(' '))]
destination = [*map(lambda x:int(x)-1,inputmethod().split(' '))]

