from threading import Thread
import random
import time

globalx = 0
def f(n):
    global globalx
    x = 0
    for _ in range(n):
        globalx+=1
    # globalx+=x

t = time.time()
val = 10_000_000
f(val)
f(val)
f(val)
f(val)
print(globalx)
globalx=0
print(time.time()-t)


x = 0
val = 10_000_000

t1 = Thread(target=f,args=(val,))
t2 = Thread(target=f,args=(val,))
t3 = Thread(target=f,args=(val,))
t4 = Thread(target=f,args=(val,))

t = time.time()
t1.start()
t2.start()
t3.start()
t4.start()

t1.join()
t2.join()
t3.join()
t4.join()

print(globalx)
globalx=0
print(time.time()-t)