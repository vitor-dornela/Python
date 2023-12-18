tiny_dict = {'a': 1, 'b': 2, 'c': 3}
 
for obj in tiny_dict:
    print(obj)
    # a
    # b
    # c

print(tiny_dict.keys())  # dict_keys(['a', 'b', 'c'])
for obj in tiny_dict.keys():
    print(obj)
    # a
    # b
    # c

print(tiny_dict.values())  # dict_values([1, 2, 3])
for obj in tiny_dict.values():
    print(obj)
    # 1
    # 2
    # 3

print(tiny_dict.items())  # dict_items([('a', 1), ('b', 2), ('c', 3)])
for obj in tiny_dict.items():
    print(obj)
    # ('a', 1)
    # ('b', 2)
    # ('c', 3)