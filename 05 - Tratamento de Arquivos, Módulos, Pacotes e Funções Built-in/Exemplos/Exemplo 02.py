#Manipulando Arquivos TXT

#Manipulando Arquivos TXT com o Pacote OS

texto = "Cientista de Dados pode ser uma excelente alternativa de carreira.\n"
texto = texto + "Esses profissiionais precisam saber como programar em Python.\n"
texto += "E, claro, devem ser proeficientes em Data Science."

print(texto)

#Importando o módulo OS
import os

#Criando um arquivo
arquivo = open(os.path.join('arquivos/cientista.txt'), 'w')

#Gravando os dados no arquivo
for palavra in texto.split():
    arquivo.write(palavra + ' ')

#Fechando o arquivo

arquivo = open('arquivos/cientista.txt', 'r')
conteudo = arquivo.read()
arquivo.close()
print(conteudo)

#Manipulando Arquivos TXT com a Expressão WITH

with open('arquivos/cientista.txt', 'r') as arquivo:
    conteudo = arquivo.read()

print(len(conteudo))

print(conteudo)

with open('arquivos/cientista.txt', 'w') as arquivo:
    arquivo.write(texto[:19])
    arquivo.write('\n')
    arquivo.write(texto[28:66])

#Lendo o arquivo

arquivo = open('arquivos/cientista.txt', 'r')
conteudo = arquivo.read()
arquivo.close()

print(conteudo)

#Manipulando Arquivos CSV

#Importando o módulo CSV

import csv

with open('arquivos/numeros.csv', 'w', newline='') as arquivo:

    #Cria o objeto de gravação
    writer = csv.writer(arquivo)

    #Grava o arquivo linha a linha
    writer.writerow(('nota1', 'nota2', 'nota3'))
    writer.writerow((63, 87, 92))
    writer.writerow((61, 79, 76))
    writer.writerow((72, 64, 91))

#Leitura de arquivos CSV

with open('arquivos/numeros.csv', 'r', encoding='utf8') as arquivo:

    #Cria o objeto de leitura
    leitor = csv.reader(arquivo)

    #Loop para imprimir cada linha do arquivo
    for x in leitor:
        print(x)

#Gerando uma lista com dados do arquivo CSV

with open('arquivos/numeros.csv', 'r') as arquivo:
    leitor = csv.reader(arquivo)
    dados = list(leitor)

print(dados)

#Imprimindo a partir da segunda linha

for linha in dados[1:]:
    print(linha)