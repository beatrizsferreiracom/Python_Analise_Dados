#Agrupamento de Dados em DataFrames com GroupBy

import pandas as pd

from pandas import DataFrame

#Primeiro importamos um dataset
dsa_df = pd.read_csv("arquivos/dataset.csv")

#Extraímos a moda da coluna Quantidade
moda = dsa_df['Quantidade'].value_counts().index[0]

#E por fim preenchemos os valores NA com a moda
dsa_df['Quantidade'].fillna(value = moda, inplace = True)

#Aplicamos o group by
g1 = dsa_df[['Segmento', 'Regiao', 'Valor_Venda']].groupby(['Segmento', 'Regiao']).mean()
print(g1)

#Agregação Múltipla com Group By

#Aplicamos o group by
g2 = dsa_df[['Segmento', 'Regiao', 'Valor_Venda']].groupby(['Segmento', 'Regiao']).agg(['mean', 'std', 'count'])
print(g2)