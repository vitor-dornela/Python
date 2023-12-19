list = ['Gohan', 'is', 'the', 'son', 'of', 'Goku']

# The sep argument is used to define how to separate the arguments
print('Gohan', 'is', 'the', 'son', 'of', 'Goku', sep=' ')
print('I', '\'m', 'all', 'together', sep='')

# But by default there's a space between the arguments
print('Gohan', 'is', 'the', 'son', 'of', 'Goku')

# The * operator unpacks the list into positional arguments, defaulting to sep=' '
print(*list)

# The end argument is used to define how to end the print statement
print(*list, end='.\n')

# The end argument can be empty so no new line is printed
print('I', ' ', 'am', ' ', 'the', 'test', sep='_', end='')
print(': no new line here')

# You can't use integers as separators
try:
    print('this', 'won\'t', 'work', sep=8)
except TypeError:
    print('TypeError: sep must be None or a string, not int')

# Separators will overwrite the default space
poem = ['The night', 'the pharmacy', 'the street', 'the pointless lamppost in the mist']
print(*poem, sep=', ', end='.')