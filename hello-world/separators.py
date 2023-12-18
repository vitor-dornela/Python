list = ['Gohan', 'is', 'the', 'son', 'of', 'Goku']

# The sep argument is used to define how to separate the arguments
print('Gohan', 'is', 'son', 'of', 'Goku', sep=' ')

# The * operator unpacks the list into positional arguments
print(*list, sep=' ')

# The end argument is used to define how to end the print statement
print(*list, end='.\n')