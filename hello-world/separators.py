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
print(*poem, sep=', ', end='.\n')

name = ['M', 'A', 'R', 'C', 'O']
print(*name, sep="-", end="!")

line1 = "Night, square, apothecary, lantern,"
line2 = "Its meaningless and pallid light."
line3 = "Return a half a lifetime after –"
line4 = "All will remain. A scapeless rite."

lines = [line1, line2, line3, line4]

# Printed in a multiple lines
for line in lines:
    print(*line, sep="") # line is a string

# Printed in a single line
print(*lines) # The default separator is a space

string = 'test'

for spacing in range(0, 5):
    print(*string, sep=' ' * spacing)
