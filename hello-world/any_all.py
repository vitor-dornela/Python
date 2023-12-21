# 0 is False, 1 (or any number) is True
predicted_temperatures = [+2, +4, -1, +0.5, -2, 0, -1]

print(any(predicted_temperatures))  # True  # any() returns True if at least one element is True
print(all(predicted_temperatures))  # False  # all() returns True if all elements are True

predicted_temperatures = [False, False, False, False, False, False, True]
print(any(predicted_temperatures))  # True]
print(all(predicted_temperatures))  # False