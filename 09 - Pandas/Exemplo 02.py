#Usando NumPy e Pandas para Manipulação de Dados

import pandas as pd

from pandas import DataFrame

#Cria um dicionário
dados = {'Estado': ['Santa Catarina', 'Rio de Janeiro', 'Tocantins', 'Bahia', 'Minas Gerais'],
         'Ano': [2004, 2005, 2006, 2007, 2008],
         'Taxa Desemprego': [1.5, 1.7, 1.6, 2.4, 2.7]}

df2 = DataFrame(dados,
                columns = ['Estado', 'Taxa Desemprego', 'Taxa Crescimento', 'Ano'],
                index = ['estado1', 'estado2', 'estado3', 'estado4', 'estado5'])

print(df2.head())

print(df2.dtypes)

#Resumo estatístico do DataFrame
print(df2.describe())

print(df2.isna())

print(df2['Taxa Crescimento'].isna())

#Importando o NumPy
import numpy as np

#Usando o NumPy para alimentar uma das colunas do dataframe
df2['Taxa Crescimento'] = np.arange(5.)

print(df2)

print(df2.dtypes)

print(df2['Taxa Crescimento'].isna())

#Resumo estatístico do DataFrame
print(df2.describe())


#Slicing de DataFrames do Pandas

#Usando o NumPy para alimentar uma das colunas do dataframe
df2['Taxa Crescimento'] = np.arange(5.)

print(df2)

print(df2['estado2':'estado4'])

print(df2[df2['Taxa Desemprego'] < 2])

print(df2[['Estado', 'Taxa Crescimento']])