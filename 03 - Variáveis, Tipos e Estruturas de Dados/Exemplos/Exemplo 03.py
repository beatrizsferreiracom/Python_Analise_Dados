#Strings e Indexação

#Criando uma String

#Uma única palavra
'Oi'

#Uma frase
'Criando uma string em Python'

#Podemos usar aspas duplas

"Podemos usar aspas duplas ou simples para strings em Python"

#Podemos combinar aspas duplas e simples
"Testando strings em 'Python'"

#Imprimindo uma String

print ('Testando Strings em Python' )

print ('Testando \nStrings \nem \nPython')

print ('\n')

#Indexando Strings

#Atribuindo uma string s = 'Data Science Academy'

s = 'Data Science Academy'

print(s)

print(s[0])
print(s[1])
print(s[2])
print(s[3])
print(s[4])

#Retorna todos os elementos da string, começando pela posição escolhida até o fim da string.

print(s[1:])

# A string original permanece inalterada
print(s)

# Retorna tudo até a posição 3
print(s[:3])

#Também podemos usar a indexação negativa e ler de trás para frente s[-1]
#Retornar tudo, exceto a última letra
print(s[-1])

print(s[::1])

print(s[::2])

print(s[::-1])

#Propriedades de Strings

print(s)

#Alterando um caracter (não é possível alterar um elemento da string) 
#s[0] = 'x' - Erro

#Concatenando strings
s = s + ' é a melhor maneira de estar preparado para o mercado de trabalho em Ciência de Dados!'

print(s)

#Podemos usar o símbolo de multiplicação para criar repetição!
letra = 'w'
letra = letra * 3

print(letra)

#Funções Built-in de Strings
print(s)

#Upper Case
print(s.upper())

#Lower Case
print(s.lower())

#Dividir uma string por espaços
print(s.split())

#Dividir uma string por um elemento específico
print(s.split('y'))

#Funções String

s = 'seja bem vindo ao universo da Linguagem Python!'

print(s.capitalize())

print(s.count('a'))

print(s.isalnum())

print(s.islower())

print(s.isspace())

print(s.endswith('o'))

#Comparando Strings

print("Python" == "R")

print("Python" == "Python")