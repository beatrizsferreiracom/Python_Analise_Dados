#Imports
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

#Carrega o dataset
df_dsa = pd.read_csv('dados/dataset.csv')

print(df_dsa.shape)

print(df_dsa.columns)

print(df_dsa.head())

print(df_dsa.info())

#Análise Exploratória - Resumo Estatístico

#Verifica se há valores ausentes
print(df_dsa.isnull().sum())

#Correlação
print(df_dsa.corr())

#Resumo estatístico do dataset
print(df_dsa.describe())

#Resumo estatístico da variável preditora
print(df_dsa["horas_estudo_mes"].describe())

#Histograma da variável preditora
sns.histplot(data = df_dsa, x = "horas_estudo_mes", kde = True)
plt.show()