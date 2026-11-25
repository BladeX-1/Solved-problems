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



tickets, customers = [*map(int,inputmethod().split(' '))]
ticketPrices = [*map(int,inputmethod().split(' '))]
ticketPrices.sort()

willingToPay = [*map(int,inputmethod().split(' '))]





exit()
dsuParent = [*range(tickets)]
# dsuParent[i] = i    initially
# it stores next available ticket

import bisect

output = []
for x in willingToPay:
    ind = bisect.bisect_right(ticketPrices,x)-1

    path = [ind]
    while(ind!=-1 and dsuParent[ind]!=ind):
        # print(ind,dsuParent)
        ind = dsuParent[ind]
        if ind != -1:
            path.append(ind)
        else:
            break

    if ind>=0:
        output.append(ticketPrices[ind])
    else:
        output.append(-1)

    for i in path:
        dsuParent[i] = max(ind-1,-1)


print(*map(str,output))
    

    



exit()
class Node:
    def __init__(self,data=-99,left=None,right=None):
        self.data = data
        self.val = data
        self.left = left
        self.right = right


def prepBST(arr,l,r):
    if l>r:
        return None
    
    m = (l+r)//2
    left = prepBST(arr,l,m-1)
    right =prepBST(arr,m+1,l)

    mid = Node(arr[m],left,right)
    return mid

# bstRoot = prepBST(ticketPrices,0,tickets-1)

def deleteMaximum(root):
    if not root.right:
        return root.left
    else:
        return deleteMaximum(root.right)
    
def findAndDeleteNearestLessEqual(root,target):
    if root.val==target:
        toReturn = root.val
        # delete root
        if not root.left:
            return (root.right,toReturn)
        root.left = deleteMaximum(root.left)

    