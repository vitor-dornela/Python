import numpy as np

def memory_size(arr):
    return arr.itemsize * arr.size # itemsize returns the length of ONE array element in bytes

arr = np.zeros((4, 3 ,2), dtype=int)  
print(memory_size(arr)) # 4 * 4 * 3 * 2 = 96 bytes