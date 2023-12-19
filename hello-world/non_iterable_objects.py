try:
    number = 42
    for digit in number:  # This will raise TypeError
        print(digit)
except TypeError:
    print('TypeError: integer is not iterable')

try:
    my_string = "Hi!"
    for char in my_string:  # This iterates over characters, not the whole string
        print(char)
except TypeError:
    print('TypeError: String is not iterable, but by default it iterates over characters')

try:
    my_bool = True
    for element in my_bool:  # This will raise TypeError
        print(element)
except TypeError:
    print('TypeError: bool is not iterable')

try:
    my_none = None
    for element in my_none:  # This will raise TypeError
        print(element)
except TypeError:
    print('TypeError: NoneType is not iterable')


try:
    my_list = [1, 2, 3]
    for item in my_list:  # This iterates over the whole list
        print(item)
except TypeError:
    print("TypeError: This won't raise a error")