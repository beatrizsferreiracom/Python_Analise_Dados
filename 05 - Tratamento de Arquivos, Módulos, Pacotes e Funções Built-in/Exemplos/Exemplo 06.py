#Função Reduce

#Importando a função reduce do módulo functools
from functools import reduce

#Criando uma lista
lista = [47, 11, 42, 13]

print(lista)

#Função
def soma(a, b):
    x = a + b
    return x

#Usando reduce com uma função e uma lista. A função vai retornar o valor máximo.
print(reduce(soma, lista))

#Criando uma lista
lst = [47, 11, 42, 13]

#Usando a função reduce() com lambda
print(reduce(lambda x, y: x + y, lst))

#Podemos atribuir a expressão lambda a uma variável
max_find2 = lambda a, b: a if (a > b) else b

print(type(max_find2))

#Reduzindo a lista até o valor máximo, através da função criada com a expressão lambda
print(reduce(max_find2, lst))


#Função Filter

#Criando uma função
def verificaPar(num):
    if num % 2 == 0:
        return True
    else:
        return False

#Chamando a função e passando um número como parâmetro. Retornará False se for ímpar e True se for par
verificaPar(35)

verificaPar(10)

lista = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18]

print(lista)

#A função filter() retorna um iterator
print(filter(verificaPar, lista))

print(list(filter(verificaPar, lista)))

print(list(filter(lambda x: x % 2 == 0, lista)))

print(list(filter(lambda num: num > 8, lista)))


#Função Zip

#Criando duas listas
x = [1, 2, 3]
y = [4, 5, 6]

#Unindo as listas. Em Python 3 retorna um iterator
print(zip(x, y))

#Perceba que zip retorna tuplas. Neste caso, uma lista de tuplas.
print(list(zip(x, y)))

#Atenção quando as sequências tiverem número diferente de elementos
print(list(zip('ABCD', 'xy')))

#Criando duas listas
a = [1, 2, 3]
b = [4, 5, 6, 7, 8]

print(list(zip(a, b)))

#Criando 2 dicionários
d1 = {'a':1, 'b':2}
d2 = {'c':3, 'd':4}

#Zip vai unir as chaves 
print(list(zip(d1, d2)))

#Zip pode unir os valores (itens)
print(list(zip(d1, d2.values())))

#Criando uma função para trocar valores entre 2 dicionários
def trocaValores(d1, d2):

    dicTemp = {}

    for d1key, d2val in zip(d1, d2.values()):
        dicTemp[d1key] = d2val

    return dicTemp

print(trocaValores(d1, d2))


#Função Enumerate

#Criando uma lista
seq = ['a', 'b', 'c']

print(enumerate(seq))

print(list(enumerate(seq)))

#Imprimindo os valores de uma lista com a função enumerate() e seus respectivos índices
for indice, valor in enumerate(seq):
    print(indice, valor)

for indice, valor in enumerate(seq):
    if indice >= 2:
        break
    else:
        print(valor)

lista = ['Marketing', 'Tecnologia', 'Business']

for i, item in enumerate(lista):
    print(i, item)

for i, item in enumerate('Data Science Academy'):
    print(i, item)

for i, item in enumerate(range(10)):
    print(i, item)