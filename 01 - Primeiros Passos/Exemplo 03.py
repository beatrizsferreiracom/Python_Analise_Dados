#GPT - Gere código Python que crie uma lista com os números entre 1 e 100 e então imprime
#os números pares, mas somente se o número for divisível por 4, com list comprehension

# Lista de números pares entre 1 e 100 que são divisíveis por 4
numeros = [x for x in range(1, 101) if x % 2 == 0 and x % 4 == 0]

# Imprimir os números
print(numeros)