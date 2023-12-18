grades = [10, 7, 8, 7, 9, 6]
print(grades)
id1 = id(grades)   
print(id1)

grades[-1] = 0
print(grades)
id2 = id(grades)
print(id2)

grades.append(0)
print(grades)
id3 = id(grades)
print(id3)

def check(obj1, obj2):
    print(obj1 is obj2)
check(grades, grades)