test_dict = {"a": 43, "b": 1233, "c": 8}

# print the key with the min/highest value
print("min: ", min(test_dict.keys(), key=test_dict.get))  # c
print("max: ", max(test_dict.keys(), key=test_dict.get))  # b

max_value = max(test_dict.values())
print(max_value)  # 1233