x = 200_000_000
y = 100_000_000

if x < y:
    print("x é maior que y")
elif x == y:
    print("x é igual a y")
elif x > y:
    print("x é maior que y")
else:
    print("x não é maior que y")

a = int(input("Digite um número: "))
b = int(input("Digite outro número: "))
minimum = a
if b < minimum:
    minimum = b
print("O menor número é ", minimum)

dictionary = ["aa", "abab", "aac", "ba", "bac", "baba", "cac", "caac"]
input_ = input()
if input_ in dictionary:
    print("Correct")
else:
    print("Incorrect")
