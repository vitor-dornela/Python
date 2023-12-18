a = "Nome"
b = "Sobrenome"
c = a + b
d = a + "\n" + b + "\n"

print(c)
print(len(c))  # tamanho da string
print(a[0])  # posição da string
print(a[0:4])  # sequencia da string *início* até *menor que*
print(a.lower())  # minúsculo
print(b.upper())  # maiúsculo
print(d)  # imprime com quebra de linhas
print(d.strip())  # retira ultima quebra de linha

minha_string = "O rato roeu a roupa do rei de Roma"
split_string = minha_string.split("r")  # quebra e remove na letra "r"

print(split_string)
print(split_string[3])  # imprime o quarto elemento da lista

busca = minha_string.find("rei")  # acha a posição da palavra
print(busca)  # imprime o numero da posição
print(minha_string[busca:])  # imprime da posição até o final
print(minha_string.find("rainha"))  # imprime -1 se não achar 
minha_string = minha_string.replace("o rei", "a rainha")
print(minha_string)

split_string = minha_string.split(" ")  # quebra e remove " "
print(split_string)
print(max(split_string))  # imprime a string com maior letra
print(min(split_string))  # imprime a string com menor letra, maiúsculo vem na frente
split_string = minha_string.lower().split()  # recebe na lista os itens em minúsculo
print(split_string)
print(min(split_string))  # imprime a string com menor letra 
