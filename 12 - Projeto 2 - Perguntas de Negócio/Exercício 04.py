#04 - Quais São as 10 Cidades com Maior Total de Vendas?
#Demonstre o resultado através de um gráfico de barras.

#Imports
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#Carrega o dataset
df_dsa = pd.read_csv('dados/dataset.csv')

#Agrupamento por cidade, cálculo do total de vendas e ordenação listando somente os 10 primeiros registros
df_maior_valor = df_dsa.groupby('Cidade')['Valor_Venda'].sum().reset_index().sort_values(by = 'Valor_Venda', ascending = False).head(10)

print(df_maior_valor.head(10))

#Plot
plt.figure(figsize = (15, 6))
sns.barplot(data = df_maior_valor, 
            y = 'Valor_Venda', 
            x = 'Cidade',
            palette = 'coolwarm').set(title = 'As 10 Cidades com Maior Total de Vendas')
plt.show()