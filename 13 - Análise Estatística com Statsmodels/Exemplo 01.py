#Regressão Linear Simples

#Construção do Modelo OLS (Ordinary Least Squares) com Statsmodels

#Imports
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import statsmodels.api as sm

#Carrega o dataset
df_dsa = pd.read_csv('dados/dataset.csv')

#Definimos a variável dependente
y = df_dsa["valor_aluguel"]

#Definimos a variável independente
X = df_dsa["area_m2"]

#O Statsmodels requer a adição de uma constante à variável independente
X = sm.add_constant(X)

#Criamos o modelo
modelo = sm.OLS(y, X)

#Treinamento do modelo
resultado = modelo.fit()
print(resultado.summary())

#Plot
plt.figure(figsize = (12, 8))
plt.xlabel("area_m2", size = 16)
plt.ylabel("valor_aluguel", size = 16)
plt.plot(X["area_m2"], y, "o", label = "Dados Reais")
plt.plot(X["area_m2"], resultado.fittedvalues, "r-", label = "Linha de Regressão (Previsões do Modelo)")
plt.legend(loc = "best")
plt.show()