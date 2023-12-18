my_tuple = (1, 2, 3)  # uma tupla é diferente de uma lista, pois é imutável
print(sum(my_tuple))

x = 1 
y = 2
print(sum((x, y)))  # sum nesse caso precisa de (()) para nao interpretar como tupla

# é útil para descarregar valores em varíaveis
a, b, c = my_tuple
print(a)  # Output: 1
print(b)  # Output: 2
print(c)  # Output: 3


# tuplas são usadas em funções que retornam vários valores
def get_name_and_age():
    return ("Alice", 30)

name, age = get_name_and_age()
print(name)  # Output: Alice
print(age)   # Output: 30

tuple_type = type(my_tuple)
print(tuple_type)  # Output: <class 'tuple'>
