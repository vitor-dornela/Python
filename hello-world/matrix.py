lists = [0, [1, [2, 3]]]
print(lists[1][1][0])   # 2


M = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(M[1][1])   # 5

# how to create a matrix
matrix = [[j for j in range(5)] for _ in range(2)]
print(matrix)

# alternatively
matrix = []  
for i in range(2): 
    # create empty row (a sublist inside our list)
    matrix.append([]) 

    for j in range(5): 
        matrix[i].append(j) 

print(matrix)

n = 5
my_list = [[1, 2] for _ in range(n)]
print(my_list)

text = [["Glitch", "is", "a", "minor", "problem", "that", "causes", "a", "temporary", "setback"],
        ["Ephemeral", "lasts", "one", "day", "only"],
        ["Accolade", "is", "an", "expression", "of", "praise"]]

input_ = 2
# list = []
# for x in text:
#     for y in x:
#         if len(y) <= input_:
#             list.append(y)

# transforming into a list comprehension to print words smaller than input
list = [y for x in text for y in x if len(y) <= input_] 
print(list)

# list comprehension with conditions to get a specific word
menu = [["pizza", 4, 20], ["soup", 1, 8], ["ice cream", 2, 4], ["toasts", 2, 10]]

what_to_order = [dish[0] for dish in menu if dish[1] >= 2 and dish[2] < 15]
print(what_to_order)

country_list = [["Moscow", "Cheboksary", "Sochi"], ["Paris", "Lyon", "Nice"],
                ["New York", "Dallas", "San Francisco"]]

# long_cities = []
# for country in country_list:
#     for city in country:
#         if len(city) >= 6:
#             long_cities.append(city)

# transforming into a list comprehension
long_cities = [city for country in country_list for city in country if len(city) >= 6]
print(long_cities)

str_1 = 'cat'
str_2 = 'dog'
str_3 = 'dragon'
my_list = [str_1, [str_2], [[str_3]]]

print(my_list[0])  # cat
print(my_list[1][0])  # dog
print(my_list[2][0][0])  # dragon