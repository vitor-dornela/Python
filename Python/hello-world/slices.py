# sequence[start:stop:step]  # from start to stop-1, by step

planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']
print(planets[2:7:2])  # ['Earth', 'Jupiter', 'Uranus']

# sequence[:end]    # elements from start to end-1
# sequence[start:]  # elements from start to the last element
# sequence[:]       # the full copy of the sequence
# sequence[::step]  # every element with a given step

snakes = ['python', 'cobra', 'viper']
print(snakes[:2])     # ['python', 'cobra']
print(snakes[0][:2])  # py

powers_of_two = [1, 2, 4, 8, 16, 32, 64, 128]
print(powers_of_two[4:])  # [16, 32, 64, 128]

colors = ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet']
print(colors[::3])  # ['red', 'green', 'violet']

pets = ['dog', 'cat', 'parrot', 'gecko']

print(pets[-2:])   # ['parrot', 'gecko']
print(pets[:-2])   # ['dog', 'cat']
print(pets[::-1])  # ['gecko', 'parrot', 'cat', 'dog']
print(pets[::-2])  # ['gecko', 'cat']

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(numbers[7:2:-1]) # [8, 7, 6, 5, 4]
print(numbers[2:7:-1])  # []
print(numbers[7:2:-2])  # [8, 6, 4]

s = "wolf"
print(s[::-1])  # flow -> start:stop:step
print(s[:-1])   # wol -> start:stop

nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# find odd numbers
print(nums[::2])  # [0, 2, 4, 6, 8]
print(nums[1::2])  # [1, 3, 5, 7, 9]
print(nums[::-2])  # [9, 7, 5, 3, 1]

numbers = [5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20,
           21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 
           36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 
           51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 
           66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80,
           81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 
           96, 97, 98, 99, 100]

# Print only divisible by 5
print(numbers[::5]) 


email = "someone@yougotmail.com";

print(email[:email.index("@")])  # someone
print(email[email.index("@")+1:])  # yougotmail.com 

print(email[:-15:1])

try:
    print(email.split('@'))
    print(email.split('@')[0])
    print(email.split('@')[1])
except IndexError:
    print(f"'{email}' is wrong email address, there's no '@' symbol found")