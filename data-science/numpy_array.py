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

# Indexing arrays
array_12 = np.array([[1, 12, 31], [4, 45, 64], [0, 7, 89]])
print("\Efficient indexing: \n",array_12[2, 2])  # 89 => more efficient
print("\Inefficient indexing: \n",array_12[2][2])  # 89 => less efficient, it creates a temporary array subsenquently indexed by 2


# Slicing arrays

array_15 = np.array([
                [[1, 2, 3, 4, 5],
                 [6, 7, 8, 9, 10]],
                [[11, 12, 13, 14, 15],
                 [16, 17, 18, 19, 20]]
                 ])
print("\nArray slices: \n",array_15[-1, :, 1:4]) # 1st dimension is the last one, 2nd dimension is all, 3rd dimension is from 1 to 4
# [[12 13 14]
#  [17 18 19]]
print("\nArray slices: \n",array_15[0, :, 1:4])
# [[2 3 4]
#  [7 8 9]]

# two-dimensional array
array_16 = np.array([
                [1, 2, 3, 4, 5],
                [5, 4, 3, 2, 1],
                [6, 7, 8, 9, 10],
                [10, 9, 8, 7, 6],
                [11, 12, 13, 14, 15]
                ])
print(array_16[::2, ::2])  # start:stop:step
# [[ 1  3  5]
#  [ 6  8 10]
#  [11 13 15]]


a = np.array([[[10, 11, 12], [13, 14, 15], [16, 17, 18]],
              [[20, 21, 22], [23, 24, 25], [26, 27, 28]],
              [[30, 31, 32], [33, 34, 35], [36, 37, 38]],
              [[40, 41, 42], [43, 44, 45], [46, 47, 48]],
              [[50, 51, 52], [53, 54, 55], [56, 57, 58]],
              [[60, 61, 62], [63, 64, 65], [66, 67, 68]],
              [[70, 71, 62], [73, 74, 65], [76, 77, 78]],
              [[80, 81, 62], [83, 84, 85], [86, 87, 88]]])


dim1 = int(input("\n1st dimension step: "))
dim2 = int(input("2nd dimension step: "))
index = int(input("Index: "))
print(a[::dim1,::dim2,index])