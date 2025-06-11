#Exercício 3 - Crie uma tupla de 4 elementos, multiplique cada elemento da tupla por 2 e guarde os resultados em uma lista

tupla = (10, 20, 30, 40)

lista = []

for i in tupla:
    multi = i * 2
    lista.append(multi)

print(lista)