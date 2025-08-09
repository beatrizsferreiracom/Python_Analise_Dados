#Aplicando Linguagem SQL na Sintaxe do Pandas com Linguagem Python

import sqlite3

import pandas as pd

#Conecta no banco de dados
con = sqlite3.connect('cap11_dsa.db')

#Abre um cursor para percorrer os dados no banco de dados
cursor = con.cursor()

#Cria uma instrução SQL
query = 'SELECT * FROM tb_vendas_dsa'

#Executa a query no banco de dados
cursor.execute(query)

#Retorna os dados da execução query
dados = cursor.fetchall()

print(dados)

#Carrega os dados como dataframe do Pandas
df = pd.DataFrame(dados, columns = ['ID_Pedido',
                                    'ID_Cliente',
                                    'Nome_Produto',
                                    'Valor_Unitario',
                                    'Unidades_Vendidas',
                                    'Custo'])

print(df.head())

#Fecha o cursor e encerra a conexão
cursor.close()
con.close()

#Calcula a média de unidades vendidas
media_unidades_vendidas = df['Unidades_Vendidas'].mean()

print(type(media_unidades_vendidas))

print(media_unidades_vendidas)

#Calcula a média de unidades vendidas por produto
media_unidades_vendidas_por_produto = df.groupby('Nome_Produto')['Unidades_Vendidas'].mean()

#Visualiza os 10 primeiros resultados
print(media_unidades_vendidas_por_produto.head(10))

#Retorna a média de unidades vendidas por produto se o valor unitário for maior que 199
media_com_condicao = df[df['Valor_Unitario'] > 199].groupby('Nome_Produto')['Unidades_Vendidas'].mean()

print(media_com_condicao)

#Calcular a média de unidades vendidas por produto, quando o valor unitário for maior que 199,
#mas somente se a média de unidades vendidas for maior que 10

#Alternativa A
mediaA = df[df['Valor_Unitario'] > 199].groupby('Nome_Produto').filter(lambda x: x['Unidades_Vendidas'].mean() > 10)
print(mediaA)

#Alternativa B
mediaB = df[df['Valor_Unitario'] > 199].groupby('Nome_Produto') \
                                       .filter(lambda x: x['Unidades_Vendidas'].mean() > 10) \
                                       .groupby('Nome_Produto')['Unidades_Vendidas'].mean()
print(mediaB)