def add(a, b, *args):
    total = a + b
    for n in args:
        total += n
    return total

# The length of `args` is 3
print(add(1, 2, 3, 4, 5))

# The length of `args` is 0
print(add(1, 2))

def will_survive(*names):
    for name in names:
        print("Will", name, "survive?")

will_survive("Daenerys Targaryen", "Arya Stark", "Brienne of Tarth")

def recipe(*args, sep=" or "):
    return sep.join(args)


print(recipe("meat", "fish"))               # meat or fish
print(recipe("meat", "fish", sep=" and "))  # meat and fish

# Using *args to unpack lists
def add(*args):
    total = 0
    for n in args:
        total += n
    return total


small_numbers = [1, 2, 3]
large_numbers = [9999999, 1111111]

print(add(*small_numbers))  # 6
print(add(*large_numbers))  # 11111110

def average_mark(*args):
    return round(sum(args) / len(args), 1)

print(average_mark(1, 2, 3, 4, 5))  # 3.0

def multiply(product, *args):
    for n in args:
        product *= n
    return product

print(multiply(1, 2, 3, 4, 5)) # 120

def concat(*strings, sep=" "):
    return sep.join(strings)

print(concat("turtle"))                # "turtle"
print(concat("cat", "dog"))            # "cat dog"
print(concat("a", "b", "c", sep=":"))  # "a:b:c"

def congratulations(*x):
    print("Happy New Year! Take care of yourself and your loved ones!", "For:", *x, sep='\n')

congratulations("Daenerys Targaryen", "Arya Stark", "Brienne of Tarth")
