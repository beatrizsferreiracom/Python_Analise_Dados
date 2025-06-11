# Exercício 9 - Crie uma list comprehension que imprima as palavras com a letra a no nome

palavras = ["maça", "coiote", "banana", "terreno", "Python"]

palavras_com_A = []

for x in palavras:
    if 'a' in x:
        palavras_com_A.append(x)

print(palavras_com_A)