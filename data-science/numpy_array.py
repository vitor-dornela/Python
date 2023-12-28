import numpy as np
# NumPy arrays are much more memory-efficient and much faster than Python lists
# NumPy arrays are homogeneous: all elements have the same type (dtype)
# NumPy arrays support vectorised operations, while Python lists don’t
# NumPy arrays are fixed in size, while Python lists are dynamic

first = np.array([1, 2, 3, 4, 5])
print("\nNumpy array: \n",first)                       # [1 2 3 4 5]
print("\nArray type: \n", type(first))                 # <class 'numpy.ndarray'>


list_a = [1, 2, 3, 4]
array_a = np.array(list_a)

print("\nList multiplication: \n", list_a * 3)                      # [1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3,4]
print("\nArray multiplication: \n", array_a * 3)                     # [ 3  6  9 12]

first = np.array([1, 2, 3, 4, 5])
second = np.array([[1, 1, 1],
                   [2, 2, 2]])

# lenght returns the size of the first dimension
# size returns the total number of elements
print("\n'first' array len and size: \n",len(first), first.size)    # 5 5 
print("\n'second' array len and size: \n",len(second), second.size)  # 2 6

ones = np.ones((3, 4)) # 3 rows, 4 columns
zeros = np.zeros((2, 3 ,2), dtype=int)          #3D array with zeros of the specified shape
rnd_arr = np.random.randint(0, 20, size=(2, 3 ,2)) #3D array with random integers from 0 to 20

print("\nArray of ones: \n", ones)
print("\nArray of zeros: \n",zeros)
print("\nArray of random numbers: \n", rnd_arr)


# Arange
# np.arange(start, stop, step)
arr = np.arange(0, 10, 2) # [0 2 4 6 8]
print("\nArange array: \n", arr)

# Linespace
# np.linspace(start, stop, num)
arr = np.linspace(0, 10, 5) # [ 0.   2.5  5.   7.5 10. ]
print("\nLinspace array: \n", arr)

# Converting numpy array to list
array_a = np.array([[1, 2], [3, 4]])
list_a = array_a.tolist()
print("\nArray: \n", array_a)
print("\nList converted from array: \n", list_a)