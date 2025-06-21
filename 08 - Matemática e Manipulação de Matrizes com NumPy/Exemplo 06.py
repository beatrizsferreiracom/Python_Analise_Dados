#Slicing (Fatiamento) de Arrays NumPy

#Importando NumPy
import numpy as dsa

#Cria um array
arr22 = dsa.diag(dsa.arange(3))

print(arr22)

arr22[1, 1]

arr22[1]

arr22[:2]

arr23 = dsa.arange(10)

print(arr23)

#[start:end:step]
print(arr23[2:9:3])

#Cria 2 arrays
a = dsa.array([1, 2, 3, 4])
b = dsa.array([4, 2, 2, 4])

#Comparação item a item
print(a == b)

#Comparação global
print(dsa.array_equal(arr22, arr23))

print(arr23.min())
print(arr23.max())

#Somando um valor a cada elemento do array
print(dsa.array([1, 2, 3]) + 1.5)

#Cria um array
arr24 = dsa.array([1.2, 1.5, 1.6, 2.5, 3.5, 4.5])

print(arr24)

#Usando o método around
arr25 = dsa.around(arr24)

print(arr25)

#Tranformando a matriz em um objeto unidimensional

#Criando um array
arr26 = dsa.array([[1, 2, 3, 4], [5, 6, 7, 8]])

print(arr26)

#"Achatando" a matriz
arr27 = arr26.flatten()

print(arr27)

#Criando um array
arr28 = dsa.array([1, 2, 3])

print(arr28)

#Repetindo os elementos de um array
print(dsa.repeat(arr28, 3))

#Repetindo os elementos de um array
print(dsa.tile(arr28, 3))

#Criando um array
arr29 = dsa.array([5, 6])

#Criando uma cópia do array
arr30 = dsa.copy(arr29)

print(arr30)