#Pacotes e Módulos

#Importando um pacote Python
import numpy

#Verificando todos os métodos e atributos disponíveis no pacote
dir(numpy)

#Usando um dos métodos do pacote Numpy
numpy.sqrt(25)

#Importando apenas um dos métodos do pacote Numpy
from numpy import sqrt

#Usando o método
sqrt(9)

#Imprimindo todos os métodos do pacote math
print((dir(numpy)))

#Help do método sqrt de pacote Numpy
#help(sqrt)

#Outros métodos

import random

print(random.choice(['Abacate', 'Banana', 'Laranja']))

print(random.sample(range(100), 10))

import statistics

dados = [2.75, 1.75, 1.25, 0.25, 0.5, 1.25, 3.5]

print(statistics.mean(dados))

print(statistics.median(dados))

import os

os.getcwd()

print(dir(os))

#Trabalhando com módulos dos pacotes (quando disponíveis)

#Importando o módulo request dp pacote urllib, usando para trazer url's para dentro do ambiente Python
import urllib.request

#Variável resposta armazena o objeto de conexão à url passada como parâmetro
resposta = urllib.request.urlopen('http://python.org')

#Objeto resposta
print(resposta)

#Chamando o método read() do objeto resposta e armazenando o código html na variável html
html = resposta.read()

#Imprimindo html
print(html)