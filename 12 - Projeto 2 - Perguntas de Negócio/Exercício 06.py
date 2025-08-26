#06 (Desafio Nível Baby) - Qual o Total de Vendas Por Segmento e Por Ano?

#Imports
import pandas as pd

#Carrega o dataset
df_dsa = pd.read_csv('dados/dataset.csv')

#Conversão da coluna de data para o tipo datetime para obter o formato adequado
df_dsa['Data_Pedido'] = pd.to_datetime(df_dsa['Data_Pedido'], dayfirst = True)

#Extração do ano com nova variável
df_dsa['Ano'] = df_dsa['Data_Pedido'].dt.year

#Total de vendas por segmento e por ano
total_vendas = df_dsa.groupby(['Ano', 'Segmento'])['Valor_Venda'].sum()

print(total_vendas)