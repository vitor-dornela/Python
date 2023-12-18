"""# Create an iterator using iter(input, ".")
iterator = iter(input, ".")

# Iterate until the user enters a period (".")
for character in iterator:
    if character == ".":
        break
    print(f"You entered: {character}")

print("Input terminated.")
"""

nums = [int(x) for x in iter(input, ".")]
print(sum(nums) / len(nums))
print(nums)
