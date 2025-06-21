#NumPy

#Importando NumPy
import numpy as dsa

dsa.__version__

#Instrução para instalar uma versão exata do pacote em Python
#!pip install numpy==[versão]

#Criando Arrays NumPy

#Array criado a partir de uma lista Python
arr1 = dsa.array([10, 21, 32, 43, 48, 15, 76, 57, 89])

print(arr1)

#Um objeto do tipo ndarray é um recipiente multidimensional de itens do mesmo tipo e tamanho
print(type(arr1))

#Verificando o formato do array
print(arr1.shape)

#Indexação em Arrays NumPy
print(arr1)

#Imprimindo um elemento específico no array
print(arr1[4])

#Indexação
print(arr1[1:4])

#Indexação
print(arr1[1:4+1])

#Cria uma lista de índices
indices = [1, 2, 5, 6]

#Imprimindo os elementos dos índices
print(arr1[indices])

#Cria uma máscara booleana para os elementos pares
mask = (arr1 % 2 == 0)

print(arr1[mask])

#Alterando um elemento do array
arr1[0] = 100

print(arr1)

#Não é possível incluir elemento de outro tipo
try:
    arr1[0] = 'Novo elemento'
except:
    print("Operação não permitida!")