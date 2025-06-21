#Manipulando Matrizes

#Importando NumPy
import numpy as dsa

#Criando uma matriz
arr9 = dsa.array([[1, 2, 3], [4, 5, 6]])

print(type(arr9))

print(arr9)

print(arr9.shape)

#Criando uma matriz 2x3 apenas com números "1"
arr10 = dsa.ones((2, 3))

print(arr10)

#Lista de listas
lista = [[13, 81, 22], [0, 34, 59], [21, 48, 94]]

#A função matrix cria uma matriz a partir de uma lista de listas
arr11 = dsa.matrix(lista)

print(type(arr11))

print(arr11)

#Formato da matriz
dsa.shape(arr11)

#Tamanho da matriz
print(arr11.size)

print(arr11.dtype)

print(arr11)

#Indexação da matriz
print(arr11[2,1])

#Indexação da matriz
print(arr11[0:2,2])

#Indexação da matriz
print(arr11[1,])

#Alterando um elemento da matriz
arr11[1, 0] = 100

print(arr11)

#Forçando o tipo de dado
x = dsa.array([1, 2]) #NumPy decide o tipo do dado (Int)
y = dsa.array([1.0, 2.0]) #NumPy decide o tipo do dado (Float)
z = dsa.array([1, 2], dtype = dsa.float64) #Forçamos um tipo de dado em particular (Int para Float)

print(x.dtype, y.dtype, z.dtype)

arr12 = dsa.array([[24, 76, 92, 14], [47, 35, 89, 2]], dtype = float)

print(arr12)

#O itemsize retorna o tamnho em bytes de cada elemento do array
print(arr12.itemsize)

print(arr12.nbytes)

print(arr12.ndim)

#Manipulando Objetos de 3 e 4 Dimensões com NumPy

#Cria um array numpy de 3 dimensões
arr_3d = dsa.array([
    [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12]
    ],
    [
        [13, 14, 15, 16],
        [17, 18, 19, 20],
        [21, 22, 23, 24]
    ]
])

print(arr_3d)

print(arr_3d.ndim)

print(arr_3d.shape)

print(arr_3d[0, 2, 1])

#Cria um array numpy de 4 dimensões
arr_4d = dsa.array([
    [
        [
            [1, 2, 3, 4, 5],
            [6, 7, 8, 9, 10],
            [11, 12, 13, 14, 15],
            [16, 17, 18, 19, 20]
        ],
        [
            [21, 22, 23, 24, 25],
            [26, 27, 28, 29, 30],
            [31, 32, 33, 34, 35],
            [36, 37, 38, 39, 40]
        ],
        [
            [41, 42, 43, 44, 45],
            [46, 47, 48, 49, 50],
            [51, 52, 53, 54, 55],
            [56, 57, 58, 59, 60]
        ]
    ],
    [
        [
            [61, 62, 63, 64, 65],
            [66, 67, 68, 69, 70],
            [71, 72, 73, 74, 75],
            [76, 77, 78, 79, 80]
        ],
        [
            [81, 82, 83, 84, 85],
            [86, 87, 88, 89, 90],
            [91, 92, 93, 94, 95],
            [96, 97, 98, 99, 100]
        ],
        [
            [101, 102, 103, 104, 105],
            [106, 107, 108, 109, 110],
            [111, 112, 113, 114, 115],
            [116, 117, 118, 119, 120]
        ]
    ]
])

print(arr_4d.ndim)

print(arr_4d.shape)

print(arr_4d[0, 2, 1])

print(arr_4d[0, 2, 1, 4])