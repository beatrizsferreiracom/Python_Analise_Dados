#Aplicando Linguagem SQL Direto no Banco de Dados com Linguagem Python

import sqlite3

#Conecta no banco de dados
con = sqlite3.connect('cap11_dsa.db')

#Abre um cursor para percorrer os dados no banco de dados
cursor = con.cursor()

#Cria uma instrução SQL para calcular a média de unidades vendidas
query2 = 'SELECT AVG(Unidades_Vendidas) FROM tb_vendas_dsa'

#Executa a query no banco de dados
cursor.execute(query2)

#Visualiza o resultado
print(cursor.fetchall())

#Cria uma instrução SQL para calcular a média de unidades vendidas por produto
query3 = 'SELECT Nome_Produto, AVG(Unidades_Vendidas) FROM tb_vendas_dsa GROUP BY Nome_Produto'

#Executa a query no banco de dados
cursor.execute(query3)

#Visualiza o resultado
print(cursor.fetchall())

#Cria uma instrução SQL para calcular a média de unidades vendidas por produto,
#quando o valor unitário for maior que 199

query4 = """SELECT Nome_Produto, AVG(Unidades_Vendidas)
            FROM tb_vendas_dsa
            WHERE Valor_unitario > 199
            GROUP BY Nome_Produto"""

#Executa a query no banco de dados
cursor.execute(query4)

#Visualiza o resultado
print(cursor.fetchall())

#Cria uma instrução SQL para calcular a média de unidades vendidas por produto,
#quando o valor unitário for maior que 199, mas somente se a média de unidades vendidas for maior que 10

query5 = """SELECT Nome_Produto, AVG(Unidades_Vendidas)
            FROM tb_vendas_dsa
            WHERE Valor_unitario > 199
            GROUP BY Nome_Produto
            HAVING AVG(Unidades_Vendidas) > 10"""

#Executa a query no banco de dados
cursor.execute(query5)

#Visualiza o resultado
print(cursor.fetchall())

#Fecha o cursor e encerra a conexão
cursor.close()
con.close()