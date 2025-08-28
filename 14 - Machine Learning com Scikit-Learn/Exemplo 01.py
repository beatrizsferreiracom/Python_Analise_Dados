#Preparação dos Dados

#Imports
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

#Carrega o dataset
df_dsa = pd.read_csv('dados/dataset.csv')

#Prepara a variável da entrada X
X = np.array(df_dsa['horas_estudo_mes'])

print(type(X))

#Ajuste no shape de X
X = X.reshape(-1, 1)

#Prepara a variável alvo
y = df_dsa['salario']

#Gráfico de dispersão entre X e y
plt.scatter(X, y, color = "blue", label = "Dados Reais Históricos")
plt.xlabel("Horas de Estudo")
plt.ylabel("Salário")
plt.legend()
plt.show()

#Dividir os dados em treinamento e teste
X_treino, X_teste, y_treino, y_teste = train_test_split(X, y, test_size = 0.2, random_state = 42)

print(X_treino.shape)

print(X_teste.shape)

print(y_treino.shape)

print(y_teste.shape)

#Modelagem Preditiva

#Cria o modelo de regressão linear simples
modelo = LinearRegression()

#Treina o modelo
modelo.fit(X_treino, y_treino)

#Visualiza a reta de regressão linear (previsões) e os dados reais usados no treinamento
plt.scatter(X, y, color = "blue", label = "Dados Reais Históricos")
plt.plot(X, modelo.predict(X), color = "red", label = "Reta de Regressão com as Previsões do Modelo")
plt.xlabel("Horas de Estudo")
plt.ylabel("Salário")
plt.legend()
plt.show()

#Avalia o modelo nos dados de teste
score = modelo.score(X_teste, y_teste)
print(f"Coeficiente R^2: {score:2f}")

#Intercepto - parâmetro w0
print(modelo.intercept_)

#Slope - parâmetro w1
print(modelo.coef_)

#Deploy do Modelo

#Define um novo valor para horas de estudo
horas_estudo_novo = np.array([[48]])

#Faz previsão com o modelo treinado
salario_previsto = modelo.predict(horas_estudo_novo)

print("Se você estudar cerca de", horas_estudo_novo, "horas por mês seu salário pode ser igual a", salario_previsto)

#Mesmo resultado anterior usando os parâmetros (coeficientes) aprendidos pelo modelo
# y = w0 + w1 * X
salario = modelo.intercept_ + (modelo.coef_ * horas_estudo_novo)
print(salario)

#Define um novo valor para horas de estudo
horas_estudo_novo = np.array([[65]])

#Faz previsão com o modelo treinado
salario_previsto = modelo.predict(horas_estudo_novo)

print("Se você estudar cerca de", horas_estudo_novo, "horas por mês seu salário pode ser igual a", salario_previsto)

#Define um novo valor para horas de estudo
horas_estudo_novo = np.array([[73]])

#Faz previsão com o modelo treinado
salario_previsto = modelo.predict(horas_estudo_novo)

print("Se você estudar cerca de", horas_estudo_novo, "horas por mês seu salário pode ser igual a", salario_previsto)