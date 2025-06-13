#Manipulação de Arquivos

#Lendo Arquivos

#Abrindo o arquivo para leitura

arq1 = open("arquivos/arquivo1.txt", "r") # r = read

type(arq1)

#Lendo o arquivo
print(arq1.read())

#Contar o número de caracteres
print(arq1.tell())

#Lendo o arquivo
print(arq1.read())

#Retornar para o iníco do arquivo
print(arq1.seek(0,0))

#Lendo os primeiros 23 caracteres
print(arq1.read(23))

#Lendo o arquivo
print(arq1.read())

#Gravando Arquivos

#Abrindo arquivo para gravação
arq2 = open("arquivos/arquivo2.txt", "w") # w = write

#Como abrimos o arquivo apenas para gravação, não podemos usar comandos de leitura.
#print(arq2.read())

#Gravando arquivo
arq2.write("Aprendendo a programar em Python.")
arq2.close()

#Lendo arquivo gravado
arq2 = open("arquivos/arquivo2.txt", "r")

print(arq2.read())

#Acrescentando conteúdo
arq2 = open("arquivos/arquivo2.txt", "a") # a = append

arq2.write(" E a metodologia de ensino da Data Science Academy facilita o aprendizado.")

arq2.close()

arq2 = open("arquivos/arquivo2.txt", "r")

print(arq2.read())

#Retornando ao início do arquivo para leitura
arq2.seek(0,0)

print(arq2.read())

#Abrindo Dataset em Linha Única

f = open('arquivos/salarios.csv', 'r')

data = f.read()

rows = data.split('\n')

print(rows)

#Dividindo Um Arquivo em Colunas

f = open('arquivos/salarios.csv', 'r')

data = f.read()

rows = data.split('\n')

full_data = []

type(rows)

for row in rows:
    split_row = row.split(",")
    full_data.append(split_row)

print(full_data)

#Contando as Linhas de Um arquivo

f = open('arquivos/salarios.csv', 'r')

data = f.read()

rows = data.split('\n')

full_data = []

for row in rows:
    split_row = row.split(",")
    full_data.append(split_row)

count = 0

for row in full_data:
    count += 1   # Equivalente a: count = count + 1
print(count)

#Contando o Número de Colunas de Um Arquivo

f = open('arquivos/salarios.csv', 'r')

data = f.read()

rows = data.split('\n')

full_data = []

for row in rows:
    split_row = row.split(",")
    full_data.append(split_row)
    first_row = full_data[0]

count = 0

for column in first_row:
    count = count + 1
    
#Outra solução possível
#   for column in full_data[0]:
#       count = count + 1

print(count)

#Importando um Dataset com Pandas

import pandas as pd

pd.__version__

arquivo = "arquivos/salarios.csv"

df = pd.read_csv(arquivo)

df.head()

df['Position Title'].value_counts()