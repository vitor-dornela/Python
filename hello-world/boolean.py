# division is never evaluated, because the first argument is True
lazy_or = True or (1 / 0)  # True
print("#1: " + str(lazy_or)) # 1

# division is never evaluated, because the first argument is False
lazy_and = False and (1 / 0)  # False
print("#2: " + str(lazy_and)) # 2

# or returns the first value if it evaluates to True, otherwise it returns the second value.
print("#3: " + str(False or 100)) # 3
print("#4: " + str("" or False)) # 4

# and returns the first value if it evaluates to False, otherwise it returns the second value.
print("#5: " + str(5 and 100)) # 5
print("#6: " + str(100 and True)) # 6

# `and` has a higher priority than `or`
truthy_integer = False or 5 and 100  # 100
print("#7: " + str(truthy_integer)) # 7

