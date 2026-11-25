import numpy as np
from matplotlib import pyplot as plt

def polyMult(p1,p2):
    p3 = [0] * (len(p1) + len(p2) - 1)
    for i in range(len(p1)):
        for j in range(len(p2)):
            p3[i + j] += p1[i] * p2[j]
    return p3

arr = [0,0,1,2,3,0]
brr = [3,3,4,5,6,3,5,6]
# fft = np.fft.fft(arr)
print(polyMult(arr, brr))
print(np.convolve(arr,brr))