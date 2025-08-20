#Import
import pandas as pd

#Carregando os Dados

#Carrega o dataset
df_dsa = pd.read_csv('dados/dataset.csv')

#Shape
print(df_dsa.shape)

#Amostra dos dados
print(df_dsa.head())

#Amostra dos dados
print(df_dsa.tail())

#Análise Exploratória

#Colunas do conjunto de dados
print(df_dsa.columns)

#Verificando o tipo de dado de cada coluna
print(df_dsa.dtypes)

#Resumo estatístico da coluna com o valor de venda
print(df_dsa['Valor_Venda'].describe())

#Verificando se há registros duplicados
print(df_dsa[df_dsa.duplicated()])

#Verificando de há valores ausentes
print(df_dsa.isnull().sum())

print(df_dsa.head())