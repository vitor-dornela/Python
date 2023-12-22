import numpy as np
# NumPy arrays are much more memory-efficient and much faster than Python lists
# NumPy arrays are homogeneous: all elements have the same type (dtype)
# NumPy arrays support vectorised operations, while Python lists don’t
# NumPy arrays are fixed in size, while Python lists are dynamic

first = np.array([1, 2, 3, 4, 5])
print(first)                       # [1 2 3 4 5]
print(type(first))                 # <class 'numpy.ndarray'>


list_a = [1, 2, 3, 4]
array_a = np.array(list_a)

print(list_a * 3)                      # [1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3,4]
print(array_a * 3)                     # [ 3  6  9 12]

first = np.array([1, 2, 3, 4, 5])
second = np.array([[1, 1, 1],
                   [2, 2, 2]])

# lenght returns the size of the first dimension
# size returns the total number of elements
print(len(first), first.size)    # 5 5 
print(len(second), second.size)  # 2 6

arr = np.zeros((4, 3 ,2), dtype=int)          #3D array with zeros of the specified shape
rnd_arr = np.random.randint(0, 20, size=(4, 3 ,2)) #3D array with random integers from 0 to 20

print(arr)
print(rnd_arr)


