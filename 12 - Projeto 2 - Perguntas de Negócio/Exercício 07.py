#07 (Desafio Nível Júnior) - Os gestores da empresa estão considerando conceder diferentes 
#faixas de descontos e gostariam de fazer uma simulação com base na regra abaixo:

#Se o Valor_Venda for maior que 1000 recebe 15% de desconto.
#Se o Valor_Venda for menor que 1000 recebe 10% de desconto.

#Quantas Vendas Receberiam 15% de Desconto?

#Imports
import pandas as pd
import numpy as np

#Carrega o dataset
df_dsa = pd.read_csv('dados/dataset.csv')

#Criação de uma nova coluna de acordo com a regra
df_dsa['Desconto'] = np.where(df_dsa['Valor_Venda'] > 1000, 0.15, 0.10)

#Total por cada valor da variável
total_por_valor = df_dsa['Desconto'].value_counts()
print(total_por_valor)

print('No total 457 vendas receberiam desconto de 15%.')