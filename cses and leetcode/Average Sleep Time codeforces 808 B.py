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



n,k = [*map(int,inputmethod().split())]
arr = [*map(int,inputmethod().split())]

window = 0
for i in range(k):
    window+=arr[i]

sum_ = 0
for r in range(k-1,n):
    if r!=k-1:
        window+=arr[r]-arr[r-k]
    sum_+=window


print(sum_/(n-k+1))