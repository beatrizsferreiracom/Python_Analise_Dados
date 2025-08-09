#Conectando no Banco de Dados com Linguagem Python

import sqlite3

#Conecta no banco de dados
con = sqlite3.connect('cap11_dsa.db')

#Abre um cursor para percorrer os dados no banco de dados
cursor = con.cursor()

#Query SQL para extrair os nomes das colunas no banco de dados
sql_query = """SELECT name FROM sqlite_master WHERE type = 'table';"""

#Executa a query
cursor.execute(sql_query)

#Visualiza o resultado
print(cursor.fetchall())

#Ceia uma instrução SQL
query1 = 'SELECT * FROM tb_vendas_dsa'

#Executa a query no banco de dados
cursor.execute(query1)

#List comprehension para visualizar os nomes das colunas
nomes_colunas = [description[0] for description in cursor.description]

#Visualiza o resultado
print(nomes_colunas)

#Retorna os dados da execução da query
dados = cursor.fetchall()

#Visualiza os dados
print(dados)