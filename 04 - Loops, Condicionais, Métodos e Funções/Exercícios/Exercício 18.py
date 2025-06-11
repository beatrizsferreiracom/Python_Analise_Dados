#Exercício 7 - Crie uma lista vazia e uma variável com valor 4. Enquanto o valor da variável for menor ou igual a 20, 
#adicione à lista, apenas os valores pares e imprima a lista

lista = []

num = 4

while num <= 20:

    if num % 2 == 0:
        lista.append(num)

    num += 1

print(lista)