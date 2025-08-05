#Filtrando DataFrame do Pandas com Base em Strings

import pandas as pd

from pandas import DataFrame

#Primeiro importamos um dataset
dsa_df = pd.read_csv("arquivos/dataset.csv")

#Extraímos a moda da coluna Quantidade
moda = dsa_df['Quantidade'].value_counts().index[0]

#E por fim preenchemos os valores NA com a moda
dsa_df['Quantidade'].fillna(value = moda, inplace = True)

#Filtramos o dataframe pela coluna Segmento com valores que iniciam com as letran 'Con'
filt1 = dsa_df[dsa_df.Segmento.str.startswith('Con')].head()
print(filt1)

#Filtramos o dataframe pela coluna Segmento com valores que terminam com as letras 'mer'
filt2 = dsa_df[dsa_df.Segmento.str.endswith('mer')].head()
print(filt2)


#Split de Strings em DataFrames do Pandas
print(dsa_df['ID_Pedido'].head())

#Split da coluna pelo caracter '-'
print(dsa_df['ID_Pedido'].str.split('-'))

#Extraindo somente o ano
print(dsa_df['ID_Pedido'].str.split('-').str[1].head())

#Fazemos o split da coluna e extraímos o item na posição 2 (índice 1)
dsa_df['Ano'] = dsa_df['ID_Pedido'].str.split('-').str[1]

#Então conferimos a nova coluna criada
print(dsa_df.head())


#Strip de Strings em DataFrames do Pandas

print(dsa_df['Data_Pedido'].head(3))

#Vamos remover os dígitos 2 e 0 à esquerda do valor da variável 'Data_Pedido'
print(dsa_df['Data_Pedido'].str.lstrip('20'))


#Replace de Strings em DataFrames do Pandas

#Substituímos os caracteres CG por AX na coluna 'ID_Cliente'
dsa_df['ID_Cliente'] = dsa_df['ID_Cliente'].str.replace('CG', 'AX')

print(dsa_df.head())


#Combinação de Strings em DataFrames do Pandas

#Concatenando strings
dsa_df['Pedido_Segmento'] = dsa_df['ID_Pedido'].str.cat(dsa_df['Segmento'], sep = '-')

print(dsa_df.head())