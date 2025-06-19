#Funções NumPy

#Importando NumPy
import numpy as dsa

#A função array() cria um array NumPy
arr2 = dsa.array([1, 2, 3, 4, 5])

print(arr2)

#Verificando o tipo do objeto
print(type(arr2))

#Usando métodos do array NumPy
print(arr2.cumsum())

print(arr2.cumprod())

#Funções para manipular objetos NumPy
#A função arange cria uma array NumPy contendo uma progressão aritmética a partir de um intervalo - start, stop, step
arr3 = dsa.arange(0, 50, 5)

print(arr3)

#Verificando o tipo do objeto
print(type(arr3))

#Formato do array
print(dsa.shape(arr3))

print(arr3.dtype)

#Cria um array preenchido com zeros
arr4 = dsa.zeros(10)

print(arr4)

#Retorna 1 nas posições em diagonal e 0 no restante
arr5 = dsa.eye(3)

print(arr5)

#Os valores passados como parâmetro, formam uma diagonal
arr6 = dsa.diag(dsa.array([1, 2, 3, 4]))

print(arr6)

#Array de valores booleanos 
arr7 = dsa.array([True, False, False, True])

print(arr7)

#Array de strings
arr8 = dsa.array(['Linguagem Python', 'Linguagem R', 'Linguagem Julia'])

print(arr8)

#Função linspace()
print(dsa.linspace(0, 10))

print(dsa.linspace(0, 10, 15))

#Função logspace()
print(dsa.logspace(0, 5, 10))