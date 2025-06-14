#Lab 3 - Expressões Regulares

import re

texto = "Meu e-mail é exemplo@gmail.com e você pode me contatar em outro_email@yahoo.com"

#Expressão regular para contar quantas vezes o caracter arroba aparece no texto
resultado = len(re.findall("@", texto))

print("O caractere '@' apareceu", resultado, "vezes no texto.")

#Expressão regular para extrair a palavra que aparece após a palavra "você" em um texto
resultado = re.findall(r'você (\w+)', texto)

print("A palavra após 'você' é:", resultado[0])

#Expressão regular para extrair endereços de e-mail de uma string
emails = re.findall(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', texto)

print(emails)

text = "O aluno estava incrivelmente perdido, mas encontrou a DSA e rapidamente começou a aprender."

#Extraindo os advérbios da frase
for m in re.finditer(r"\w+mente\b", text):
    print('%02d-%02d: %s' % (m.start(), m.end(), m.group(0)))

#REGEZ com ChatGPT

#Música Tempo Perdido, Legião Urbana

#Variável do tipo string

musica = '''
Todos os dias quando acordo
Não tenho mais
O tempo que passou
Mas tenho muito tempo
Temos todo o tempo do mundo
Todos os dias
Antes de dormir
Lembro e esqueço
Como foi o dia
Sempre em frente
Não temos tempo a perder
Nosso suor sagrado
É bem mais belo
Que esse sangue amargo
E tão sério
E selvagem! Selvagem!
Selvagem!
Veja o sol
Dessa manhã tão cinza
A tempestade que chega
É da cor dos teus olhos
Castanhos
Então me abraça forte
E diz mais uma vez
Que já estamos
Distantes de tudo
Temos nosso próprio tempo
Temos nosso próprio tempo
Temos nosso próprio tempo
Não tenho medo do escuro
Mas deixe as luzes
Acesas agora
O que foi escondido
É o que se escondeu
E o que foi prometido
Ninguém prometeu
Nem foi tempo perdido
Somos tão jovens
Tão jovens! Tão jovens!
'''

print(musica)

#1- Crie um REGEX para contar quantas vezes o caracter "a" aparece em todo o texto da música. (GPT)
match = re.findall("a", musica)
count = len(match)
print("O caractere 'a' aparece", count, "vezes no texto.")

# 1- Crie um REGEX para contar quantas vezes o caracter "a" aparece em todo o texto da música.
resultado1 = len(re.findall("a", musica))
print("O caractere 'a' apareceu", resultado1, "vezes na música.")

#2- Crie um REGEX em Python para contar quantas vezes a palavra tempo aparece na música. (GPT)
match = re.findall(r"\btempo\b", musica)
count = len(match)
print("A palavra 'tempo' aparece", count, "vezes no texto.")

#2- Crie um REGEX em Python para contar quantas vezes a palavra tempo aparece na música.
resultado2 = len(re.findall("tempo", musica))
print("A palavra 'tempo' apareceu", resultado2, "vezes na música.")

#3- Crie um REGEX em Python para extrair as palavras seguidas por exclamação. (GPT)
match = re.findall(r"\b\w+!\b", musica)
print("As palavras seguidas por exclamação são:", match)

#3- Crie um REGEX em Python para extrair as palavras seguidas por exclamação.
resultado3 = re.findall(r'\b\w+!', musica)
print("Estas são as palavras seguidas por exclamação:", resultado3)

#4- Crie um REGEX que extrai qualquer palavra cujo antecessor seja a palavra "esse" e o sucessor seja a palavra "amargo" em um texto. (GPT)
resultado = re.findall(r"esse\s(\w+)\samargo", musica)
print("Palavras entre 'esse' e 'amargo':", resultado)

#4- Crie um REGEX que extrai qualquer palavra cujo antecessor seja a palavra "esse" e o sucessor seja a palavra "amargo" em um texto.
resultado4 = re.findall(r'\besse\s(\w+)\samargo\b', musica)
print("Palavra(s) encontrada(s):", resultado4)

#5- Crie um REGEX que retorne as palavras com acento, mas somente os caracteres na palavra que são anteriores ao caracter com acento. (GPT)
resultado = re.findall(r"(\w+)\b[áéíóú]", musica)
print("Partes das palavras com acentos:", resultado)

#5- Crie um REGEX que retorne as palavras com acento, mas somente os caracteres na palavra que são anteriores ao caracter com acento. (GPT)
resultado = re.findall(r"(\w+)[\u00C0-\u017F]+", musica)
print("Palavras com acento, sem o acento:", resultado)

#5- Crie um REGEX que retorne as palavras com acento, mas somente os caracteres na palavra que são anteriores ao caracter com acento.
resultado5 = re.findall(r'\b[\wÀ-ÿ]+[áéíóúãõç]', musica)
print("As palavras acentuadas são:", resultado5)