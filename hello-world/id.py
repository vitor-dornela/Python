grades = [10, 7, 8, 7, 9, 6]
print(grades)
# Get the memory address of the list
id1 = id(grades)   
print(id1)

grades[-1] = 0
print(grades)
# id2 gets the memory address of id1
id2 = id(grades)
print(id2)

# Even if you change the list, the memory address remains the same
grades.append(0)
print(grades)
id3 = id(grades)
print(id3)

# If you create a new list, the memory address changes
grades.append(0)
id4 = id(grades)
print(id4)

# Copying a list
grades2 = grades.copy()  # Create a copy with different memory address
grades2.pop()  # Remove the last element from the grades2 list
grades.pop()
print(grades)
print(id(grades2))
print(grades2)
# Check if two objects have the same memory address, "==" just checks if the values are the same
def check(obj1, obj2):
    print(obj1 is obj2)

# Even if the values are the same, the memory address is different
check(grades, grades2)