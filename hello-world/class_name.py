# using split and join
class_name = input().split("_")
formatted_class_name = "".join(word.capitalize() for word in class_name)
print(formatted_class_name)

# faster way
print(input().title().replace("_",""))