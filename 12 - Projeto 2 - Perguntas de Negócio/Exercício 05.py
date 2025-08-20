#05 - Qual Segmento Teve o Maior Total de Vendas?
#Demonstre o resultado através de um gráfico de pizza.

#Imports
import pandas as pd
import matplotlib.pyplot as plt

#Carrega o dataset
df_dsa = pd.read_csv('dados/dataset.csv')

#Agrupamento por segmento e cálculo do total de vendas
df_total_segmento = df_dsa.groupby('Segmento')['Valor_Venda'].sum().reset_index().sort_values(by = 'Valor_Venda', ascending = True)

#Função para converter os dados em valor absoluto
def autopct_format(values): 
    def my_format(pct): 
        total = sum(values) 
        val = int(round(pct * total / 100.0))
        return ' $ {v:d}'.format(v = val)
    return my_format

#Plot
plt.figure(figsize = (10, 6))
plt.pie(df_total_segmento['Valor_Venda'], 
        labels = df_total_segmento['Segmento'],
        autopct = autopct_format(df_total_segmento['Valor_Venda']),
        startangle = 90)

#Labels e anotações
plt.annotate(text = 'Total de Vendas: ' + '$ ' + str(int(sum(df_total_segmento['Valor_Venda']))), xy = (-0.5, -1.25))
plt.title('Total de Vendas Por Segmento')
plt.show()