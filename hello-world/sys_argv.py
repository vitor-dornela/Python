import sys  

# sys.argv is a list in Python, which contains the command-line arguments passed to the script.
args = sys.argv  

# If the user does not provide exactly two arguments, print an error message and exit
if len(args) != 3: # The first argument is the name of the script
    print("The script should be called with two arguments, the first and the second number to be multiplied")

else:
    first_num = float(args[1])  
    second_num = float(args[2])

    product = first_num * second_num

    print("The product of " + args[1] + " times " + args[2] + " equals " + str(product))

# Run this script from the command line as follows:
# python sys_argv.py 2 3