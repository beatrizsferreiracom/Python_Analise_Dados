#Preenchendo Valores Ausentes em Data Frames do Pandas

import pandas as pd

from pandas import DataFrame

#Primeiro importamos um dataset
dsa_df = pd.read_csv("arquivos/dataset.csv")

print(dsa_df.head(5))

print(dsa_df.isna().sum())

#Extraímos a moda da coluna Quantidade
moda = dsa_df['Quantidade'].value_counts().index[0]

print(moda)

#E por fim preenchemos os valores NA com a moda
dsa_df['Quantidade'].fillna(value = moda, inplace = True)

print(dsa_df.isna().sum())


#Query (Consulta) de Dados no DataFrame do Pandas

#Checamos os valores mínimo e máximo da coluna Valor_Venda
print(dsa_df.Valor_Venda.describe())

#Geramos um novo dataframe apenas com o intervalo de vendas entre 229 e 10000
df2 = dsa_df.query('229 < Valor_Venda < 10000')

#Então confirmamos os valores mínimo e máximo
print(df2.Valor_Venda.describe())

#Geramos um novo dataframe apenas com os valores de venda acima da média
df3 = df2.query('Valor_Venda > 766')

print(df3.head())


#Verificando a Ocorrência de Diversos Valores em uma Coluna
print(dsa_df.shape)

#Então aplicamos o filtro
print(dsa_df[dsa_df['Quantidade'].isin([5,7,9,11])])

#Shape
print(dsa_df[dsa_df['Quantidade'].isin([5,7,9,11])].shape)

print(dsa_df[dsa_df['Quantidade'].isin([5,7,9,11])][:10])


#Operadores Lógicos para Manipulação de Dados com Pandas

#Filtrando as vendas que ocorreram para o segmento de Home Office e na região South
seg1 = dsa_df[(dsa_df.Segmento == 'Home Office') & (dsa_df.Regiao == 'South')].head()
print(seg1)

#Filtrando as vendas que ocorreram para o segmento de Home Office ou na região South
seg2 = dsa_df[(dsa_df.Segmento == 'Home Office') | (dsa_df.Regiao == 'South')].head()
print(seg2)

#Filtrando as vendas que nao ocorreram para o segmento de Home Office nem região South
seg3 = dsa_df[(dsa_df.Segmento != 'Home Office') & (dsa_df.Regiao != 'South')].sample(5)
print(seg3)