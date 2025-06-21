#Análise Estatística com NumPy

#Importando NumPy
import numpy as dsa

#Criando um Array
arr14 = dsa.array([15, 23, 63, 94, 75])

#Média
print(dsa.mean(arr14))

#Desvio padrão
print(dsa.std(arr14))

#Variância
print(dsa.var(arr14))
 
#Operações Matemáticas com Arrays NumPy

arr15 = dsa.arange(1, 10)

print(arr15)

#Soma dos elementos do array
print(dsa.sum(arr15))

#Retorna o produto dos elementos
print(dsa.prod(arr15))

#Soma acumulada dos elementos
print(dsa.cumsum(arr15))

#Cria 2 arrays
arr16 = dsa.array([3, 2, 1])
arr17 = dsa.array([1, 2, 3])

#Soma dos arrays
arr18 = dsa.add(arr16, arr17)

print(arr18)

#Multiplicação de matrizes

#Cria duas matrizes
arr19 = dsa.array([[1, 2], [3, 4]])
arr20 = dsa.array([[5, 6], [0, 7]])

print(arr19.shape)
print(arr20.shape)

print(arr19)
print(arr20)

#Multiplicar as duas matrizes
arr21 = dsa.dot(arr19, arr20)

print(arr21)

#Multiplicar as duas matrizes
arr21 = arr19 @ arr20

print(arr21)

#Multiplicar as duas matrizes
arr21 = dsa.tensordot(arr19, arr20, axes = ((1), (0)))

print(arr21)