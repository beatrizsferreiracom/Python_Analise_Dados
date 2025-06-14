#Manipulando Arquivos JSON (Java Script Object Notation)

#Criando um dicionário
dict_guido = {'nome': 'Guido van Rossum',
              'linguagem': 'Python',
              'similar': ['c', 'Modula-3', 'lisp'],
              'users': 1000000}

for k,v in dict_guido.items():
    print(k,v)

#Importando o módulo JSON
import json

#Convertendo o dicionário para um objeto json
json.dumps(dict_guido)

#Criando um arquivo Json

with open('arquivos/dados.json', 'w') as arquivo:
    arquivo.write(json.dumps(dict_guido))

#Leitura de arquivos Json

with open('arquivos/dados.json', 'r') as arquivo:
    texto = arquivo.read()
    dados = json.loads(texto)

print(dados)

print(dados['nome'])

#Extração de Arquivo da Web

#Imprimindo um arquivo JSON copiado da internet

from urllib.request import urlopen

response = urlopen("http://vimeo.com/api/v2/video/57733101.json").read().decode('utf8')
dados = json.loads(response)[0]

print(dados)

print("Título: ", dados['title'])
print("URL: ", dados['url'])
print("Duração: ", dados['duration'])
print("Número de visualizações: ", dados['stats_number_of_plays'])

#Copiando o conteúdo de um arquivo para outro

#Nomes dos arquivos

arquivo_fonte = 'arquivos/dados.json'
arquivo_destino = 'arquivos/dados.txt'

#Método 1

with open(arquivo_fonte, 'r') as infile:
    text = infile.read()
    with open(arquivo_destino, 'w') as outfile:
        outfile.write(text)

#Método 2

open(arquivo_destino, 'w').write(open(arquivo_fonte, 'r').read())

#Leitura arquivo txt

with open('arquivos/dados.txt', 'r') as arquivo:
    texto = arquivo.read()
    dados = json.loads(texto)

print(dados)