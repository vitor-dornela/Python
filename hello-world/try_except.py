# You can't use integers as separators
try:
    print('this', 'won\'t', 'work', sep=8)
except TypeError:
    print('TypeError: sep must be None or a string, not int')

try:
    price = int(input('Enter a new price: '))  # $451
    print(price)
except ValueError:
    print('ErrorValue: Please enter an integer value.')
