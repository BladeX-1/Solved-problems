import sys
# inputI = -1
# inputArr = []
try:
    open("__localsystemflag__").close()
    f = open('inp.txt')
    env = 'local'
except FileNotFoundError:
    # inputArr = sys.stdin.read().split('\n')
    # inputI = 0
    f = None
    env = 'server'

def inputmethod():
    # global inputI
    if f:
        return f.readline().strip()
    else:
        # inputI+=1
        # return inputArr[inputI-1]
        return input()





t = int(inputmethod())
# t = 1
from collections import defaultdict as dd
for _ in range(t):
    n = int(inputmethod())
    arr = [*map(int,inputmethod().split(' '))]
    arrSum = sum(arr)

    if n==1:
        print("!",1)
        continue

    quantity2i = dd(list)
    for i,x in enumerate(arr):
        quantity2i[x].append(i+1)

    if len(quantity2i)>1:
        
        print("?",*arr)

        sum_ = int(inputmethod())
        bagQuantity = (arrSum*7-sum_)
    else:
        bagQuantity = arr[0] # if all are equal

    interestedI = quantity2i[bagQuantity]

    while(True):
        l = len(interestedI)
        if l==1:
            print("!",interestedI[0])
            break
        windowLength = l//(bagQuantity+1)

        toPrint = [0]*n
        quantity = bagQuantity+1
        mySum = 0
        myMap = dd(list)
        for i in range(l):
            if i%windowLength==0:
                quantity -= 1
            toPrint[interestedI[i]-1] = quantity
            myMap[quantity].append(interestedI[i])
            mySum+=quantity*7

        print("?",*toPrint)
        sum_ = int(inputmethod())
        ans = (mySum-sum_)
        # print('ans',ans)
        if ans==0:
            left = l-l%windowLength
            right = l-1
            interestedI = interestedI[left:right+1]
        else:
            interestedI = myMap[ans]

