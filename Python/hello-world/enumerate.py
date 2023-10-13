# The description is wrong.  It should be something like this :  Write a program that takes in 2 inputs 
# the first input is a list of numbers and the 2nd one is a number you are looking for in the list. 
# Print the indexes of the found numbers. 
input_string = input("Digite uma lista de números com espaços: ")
input_list = input_string.split()
number = input("Digite um número para achar na lista: ")
output = []

# Convert the input_list elements to integers
input_list = [int(item) for item in input_list]

# Uses enumerate to iterate over index and value (start is optional)
for index, value in enumerate(input_list, start=0):
    if value == int(number):
        output.append(str(index))
        
if not output: # checks if output == []
    print("Nenhum número foi achado")
else:
    result = " ".join(output) # create a space between numbers
    print("O número se encontra no(s) index(s): " + result)
