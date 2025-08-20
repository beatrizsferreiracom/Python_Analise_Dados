#02 - Qual o Total de Vendas Por Data do Pedido?
#Demonstre o resultado através de um gráfico de barras.

#Imports
import pandas as pd
import matplotlib.pyplot as plt

#Carrega o dataset
df_dsa = pd.read_csv('dados/dataset.csv')

#Cálculo do total de vendas para cada data de pedido
df_total_data = df_dsa.groupby('Data_Pedido')['Valor_Venda'].sum()

print(df_total_data.head())

#Gráfico
plt.figure(figsize = (15, 6))
df_total_data.plot(x = 'Data_Pedido', y = 'Valor_Venda', color = 'purple')
plt.title('Total de Vendas por Data do Pedido')
plt.show()