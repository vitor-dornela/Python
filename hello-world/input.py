# Simple input example
numero = input("Insira um número: ")
print("Seu número é " + numero)

# Advanced input to multiple variables  
gift, recipient = input("Insert both gift and recipient (separated by space):").split()
print(f'{gift} for {recipient}')
