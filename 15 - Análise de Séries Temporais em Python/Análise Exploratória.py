#Análise de Séries Temporais em Python

#Imports
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from statsmodels.tsa.holtwinters import SimpleExpSmoothing

#Carregando os Dados

#Carrega o dataset
df_dsa = pd.read_csv('dados/dataset.csv')

print(df_dsa.shape)

print(df_dsa.columns)

print(df_dsa.head())

print(df_dsa.tail())

#Pré-Processamento dos Dados

#Valor mínimo da coluna data
print(df_dsa['Data'].min())

#Valor máximo da coluna data
print(df_dsa['Data'].max())

print(df_dsa.info())

#Converte a coluna de data no tipo datetime
df_dsa['Data'] = pd.to_datetime(df_dsa['Data'])

print(df_dsa.head())

print(df_dsa.info())

#Converter o DataFrame em uma série temporal com a data como índice
serie_temporal = df_dsa.set_index('Data')['Total_Vendas']

print(type(serie_temporal))

print(serie_temporal)

#Fornece a frequência da série temporal (diária, neste caso)
serie_temporal = serie_temporal.asfreq('D')

print(serie_temporal)

#Análise Exploratória

#Cria o gráfico da série temporal (sem formatação)
plt.figure(figsize = (12, 6))
plt.plot(serie_temporal)
plt.xlabel('Data')
plt.ylabel('Vendas')
plt.title('Série Temporal de Vendas')
plt.grid(True)
plt.show()

#Cria o gráfico da série temporal (com formatação)

#Criar o gráfico da série temporal com layout de contraste
plt.figure(figsize = (12, 6))
plt.plot(serie_temporal, color = 'white', linewidth = 2)

#Configurar cores e estilo do gráfico
plt.gca().set_facecolor('#2e03a3')
plt.grid(color = 'yellow', linestyle = '--', linewidth = 0.5)

#Configurar rótulos dos eixos, título e legenda
plt.xlabel('Data', color = 'black', fontsize = 14)
plt.ylabel('Vendas', color ='black', fontsize = 14)
plt.title('Série Temporal de Vendas', color = 'black', fontsize = 18)

#Configurar as cores dos eixos e dos ticks (marcadores)
plt.tick_params(axis = 'x', colors  ='black')
plt.tick_params(axis = 'y', colors = 'black')

plt.show()