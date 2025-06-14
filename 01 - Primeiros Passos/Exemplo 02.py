#Lab 2 - Usando o ChatGPT

#GPT - Gere código Python que crie uma lista com os números entre 1 e 100 
#e então imprime os números pares, mas somente se o número for divisível por 4

# Criar a lista de números de 1 a 100
numeros = list(range(1, 101))

# Iterar sobre a lista e imprimir apenas os pares divisíveis por 4
for numero in numeros:
    if numero % 2 == 0 and numero % 4 == 0:
        print(numero)
