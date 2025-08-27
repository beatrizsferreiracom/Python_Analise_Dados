#Imports
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import statsmodels.api as sm

#Carrega o dataset
df_dsa = pd.read_csv('dados/dataset.csv')

#Shape
print(df_dsa.shape)

#Colunas do conjunto de dados
print(df_dsa.columns)

#Amostra dos dados
print(df_dsa.head())

#Informações sobre as colunas do dataframe
print(df_dsa.info())

#Análise Exploratória - Resumo Estatístico

#Verifica se há valores ausentes
print(df_dsa.isnull().sum())

#Resumo estatístico do dataset - ATENÇÃO
print(df_dsa.describe())

#Resumo estatístico da variável alvo
print(df_dsa['valor_aluguel'].describe())

#Histograma da variável alvo
sns.histplot(data = df_dsa, x = "valor_aluguel", kde =  True)
plt.show()

#Correlação entre as variáveis
print(df_dsa.corr())

#Vamos analisar a relação entre a variável de entrada area_m2 e a variável alvo valor_aluguel
sns.scatterplot(data = df_dsa, x = "area_m2", y = "valor_aluguel")
plt.show()