# # list comprehension syntax
# new_list = [x for x in some_iterable]

# # the equivalent code
# new_list = []
# for x in some_iterable:
#     new_list.append(x)

# # list comprehension with condition
# new_list = [x for x in some_iterable if condition]


words = ["apple", "it", "creek", "pelican", "subsequent", "horse",
         "apothecary"]
list_lengths = [len(word) for word in words]
print(list_lengths)


vowels = 'aeiou'
vowels_list = [x for x in input() if x in vowels]
print(vowels_list)

# the following line reads the list from the input, do not modify it, please
old_list = [int(num) for num in input().split()]
binary_list = [1 if x > 0 else  0 for x in old_list]
print(binary_list)

# a list divisible by 3 from a range of 1 to 1000
divisible_by_3 = [x for x in range(1, 1000) if x % 3 == 0]
print(divisible_by_3)
