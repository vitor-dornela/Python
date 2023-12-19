# You can't use integers as separators
try:
    print('this', 'won\'t', 'work', sep=8)
except TypeError:
    print('TypeError: sep must be None or a string, not int')