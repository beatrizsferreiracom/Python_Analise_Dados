#Manipulando Arquivos com NumPy

#Importando NumPy
import numpy as dsa

import os

filename = os.path.join('arquivos/dataset.csv')

#Carregando um dataset para dentro de um array
arr13 = dsa.loadtxt(filename, delimiter = ',', usecols = (0, 1, 2, 3), skiprows = 1)

print(arr13)

print(type(arr13))

#Carregando apenas duas variáveis (colunas) do arquivo
var1, var2 = dsa.loadtxt(filename, delimiter = ',', usecols = (0, 1), skiprows = 1, unpack = True)

#Gerando um plot a partir de um arquivo usando o NumPy
import matplotlib.pyplot as plt

plt.plot(var1, var2, 'o', markersize = 6, color = 'red')
plt.show()