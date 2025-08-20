#01 - Qual Cidade com Maior Valor de Venda de Produtos da Categoria 'Office Supplies'?

#Import
import pandas as pd

#Carrega o dataset
df_dsa = pd.read_csv('dados/dataset.csv')

#Filtro por categoria
df_categoria = df_dsa[df_dsa['Categoria'] == 'Office Supplies']

#Soma pela categoria agrupada pela cidade
df_categoria_soma = df_categoria.groupby('Cidade')['Valor_Venda'].sum()

#Selecionando o maior valor
cidadeMaior = df_categoria_soma.idxmax()

print("A cidade com o maior valor de vendas de produtos em Office Supplies:", cidadeMaior)