#03 - Qual o Total de Vendas por Estado?
#Demonstre o resultado através de um gráfico de barras.

#Imports
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#Carrega o dataset
df_dsa = pd.read_csv('dados/dataset.csv')

#Cálculo do total de vendas para cada data de pedido
df_total_estado = df_dsa.groupby('Estado')['Valor_Venda'].sum()

print(df_total_estado.head())

#Gráfico
plt.figure(figsize = (20, 6))
df_total_estado.plot(x = 'Estado', y = 'Valor_Venda', kind = 'bar', color = 'purple')
plt.title('Total de Vendas por Estado')
plt.show()

#Com Seaborn

#Agrupamento por estado e cálculo do total de vendas
df_total_estado2 = df_dsa.groupby('Estado')['Valor_Venda'].sum().reset_index()

#Plot
plt.figure(figsize = (16, 6))
sns.barplot(data = df_total_estado2, 
            y = 'Valor_Venda', 
            x = 'Estado').set(title = 'Total de Vendas Por Estado')
plt.xticks(rotation = 80)
plt.show()