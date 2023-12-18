groups = ['1A', '1B', '1C', '2A', '2B', '2C', '3A', '3B', '3C']
groups_dict = {key: None for key in groups} # Create a dictionary with None attributes

count = int(input("Enter the number of items to change: "))

# for i, key in enumerate(groups):
#     if i < count:
#         value = int(input("Enter the value: "))
#         groups_dict[key] = value

for i in range(count):
    groups_dict[groups[i]] = int(input("Enter value: "))

print(groups_dict)
