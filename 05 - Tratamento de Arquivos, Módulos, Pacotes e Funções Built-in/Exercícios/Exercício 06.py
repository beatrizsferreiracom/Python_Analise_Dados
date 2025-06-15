#Exercício 6 - Considerando o range de valores abaixo, use a função filter() para retornar 
#apenas os valores negativos.

negativos = list(filter(lambda x: x < 0, range(-5, 5)))

print(negativos)