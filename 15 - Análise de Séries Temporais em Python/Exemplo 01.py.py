#Suavização Exponencial

#Imports
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from statsmodels.tsa.holtwinters import SimpleExpSmoothing

#Carregando os Dados

#Carrega o dataset
df_dsa = pd.read_csv('dados/dataset.csv')

#Converte a coluna de data no tipo datetime
df_dsa['Data'] = pd.to_datetime(df_dsa['Data'])

#Converter o DataFrame em uma série temporal com a data como índice
serie_temporal = df_dsa.set_index('Data')['Total_Vendas']

#Cria o modelo
modelo = SimpleExpSmoothing(serie_temporal)

#Treinamento (ajuste) do modelo
modelo_ajustado = modelo.fit(smoothing_level = 0.2)

#Extrai os valores previstos pelo modelo
suavizacao_exponencial = modelo_ajustado.fittedvalues

#Plot
plt.figure(figsize = (12, 6))
plt.plot(serie_temporal, label = 'Valores Reais')
plt.plot(suavizacao_exponencial, label = 'Valores Previstos', linestyle = '--')
plt.xlabel('Data')
plt.ylabel('Vendas')
plt.title('Modelo de Suavização Exponencial')
plt.legend()
plt.show()

#Deploy e Previsão com o Modelo Treinado

#Fazer previsões
num_previsoes = 1
previsoes = modelo_ajustado.forecast(steps = num_previsoes)

print('Previsão do Total de Vendas Para Janeiro/2024:', round(previsoes[0], 4))