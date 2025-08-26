#09 (Desafio Nível Master Ninja) - Qual a Média de Vendas Por Segmento, Por Ano e Por Mês?
#Demonstre o resultado através de gráfico de linha.

#Imports
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#Carrega o dataset
df_dsa = pd.read_csv('dados/dataset.csv')

#Conversão da coluna de data para o tipo datetime para obter o formato adequado
df_dsa['Data_Pedido'] = pd.to_datetime(df_dsa['Data_Pedido'], dayfirst = True)

#Extração do ano com nova variável
df_dsa['Ano'] = df_dsa['Data_Pedido'].dt.year

#Extração do mês com nova variável
df_dsa['Mes'] = df_dsa['Data_Pedido'].dt.month

#Total de vendas por segmento e por ano
media_vendas = df_dsa.groupby(['Ano', 'Mes', 'Segmento',])['Valor_Venda'].mean().reset_index()

#Criação de uma coluna de data combinada para o eixo x
media_vendas['Mes_Ano'] = pd.to_datetime(media_vendas['Ano'].astype(str) + '-' + media_vendas['Mes'].astype(str), format='%Y-%m')

# Plot corrigido
plt.figure(figsize=(15, 6))
sns.lineplot(data=media_vendas,
             x='Mes_Ano',
             y='Valor_Venda',
             hue='Segmento',
             palette='coolwarm').set(title='Média de Vendas por Segmento, por Ano e por Mês')

plt.xlabel('Ano e Mês')
plt.ylabel('Média de Vendas')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()