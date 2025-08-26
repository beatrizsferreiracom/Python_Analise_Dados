#08 - (Desafio Nível Master) - Considere Que a Empresa Decida Conceder o Desconto de 15% da Questão Anterior. 
#Qual Seria a Média do Valor de Venda Antes e Depois do Desconto?

#Imports
import pandas as pd
import numpy as np

#Carrega o dataset
df_dsa = pd.read_csv('dados/dataset.csv')

#Criação de uma nova coluna de acordo com a regra
df_dsa['Desconto'] = np.where(df_dsa['Valor_Venda'] > 1000, 0.15, 0.10)

#Criação de uma coluna calculando o valor de venda menos o desconto (Valor_Final)
df_dsa['Valor_Final'] = df_dsa['Valor_Venda'] - (df_dsa['Valor_Venda'] * df_dsa['Desconto'])

#Filtro do valor inicial das vendas, antes do desconto de 15%
valor_inicial = df_dsa.loc[df_dsa['Desconto'] == 0.15, 'Valor_Venda']

#Filtro do valor final das vendas, depois do desconto de 15%
valor_final = df_dsa.loc[df_dsa['Desconto'] == 0.15, 'Valor_Final']

#Cálculo da média de vendas antes do desconto
media_valor_inicial = valor_inicial.mean()

#Cálculo da média de vendas depois do desconto
media_valor_final = valor_final.mean()

print("Média das vendas antes do desconto de 15%:", round(media_valor_inicial, 2))
print("Média das vendas depois do desconto de 15%:", round(media_valor_final, 2))