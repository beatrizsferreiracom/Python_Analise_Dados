#Funções

print('Hello World')

#Definindo uma função

def primeiraFunc():
    print('Hello World')

primeiraFunc()

#Definindo uma função

def primeiraFunc():
    nome = 'Bob'
    print('Hello %s' %(nome))

primeiraFunc()

#Definindo uma função com parâmetro

def segundaFunc(nome):
    print('Hello %s' %(nome))

segundaFunc('Aluno')

#Função para imprimir números

def imprimeNumeros():
    
    # Loop
    for i in range(0, 5):
        print("Número " + str(i))

imprimeNumeros()

#Função para somar números

def addNum(firstnum, secondnum):
    print("Primeiro número: " + str(firstnum))
    print("Segundo número: " + str(secondnum))
    print("Soma: ", firstnum + secondnum)

#Chamando a função e passando parâmetros
addNum(4, 7)

#Chamando a função e passando parâmetros
addNum(45, 3)

#Funções com número variável de argumentos

def printVarInfo( arg1, *vartuple ):
    
   #Imprimindo o valor do primeiro argumento
    print ("O parâmetro passado foi: ", arg1)
   
   #Imprimindo o valor do segundo argumento 
    for item in vartuple:
        print ("O parâmetro passado foi: ", item)
    return;

#Fazendo chamada à função usando apenas 1 argumento
printVarInfo(10)

printVarInfo('Chocolate', 'Morango')

printVarInfo('Data', 'Science', 'Academy')

#Escopo de Variável  - Local e Global

#Variável Global
var_global = 10  #Esta é uma variável global

#Função

def multiplica_numeros(num1, num2):
    var_global = num1 * num2  #Esta é uma variável local
    print(var_global)

multiplica_numeros(5, 25)

print(var_global)

#Variável Global
var_global = 10  # Esta é uma variável global

#Função

def multiplica_numeros(num1, num2):
    var_local = num1 * num2   # Esta é uma variável local
    print(var_local)

multiplica_numeros(5, 25)

print(var_global)

#Funções Built-in

print(abs(-56))
print(abs(23))
print(bool(0))
print(bool(1))
print(int(4.3))
print(str(13))
print(float(5))

#Erro ao executar por causa da conversão

#idade = input("Digite sua idade: ") - String não pode ser comparada com número

idade = int(input("Digite sua idade: "))

if idade > 13:
    print("Você pode acessar Redes Sociais sem supervisão!")  
else:
    print("Seus pais não deveriam você acessar Redes Sociais sem supervisão!")  

#Usando a função int para converter o valor digitado

idade = int(input("Digite sua idade: "))

if idade > 13:
    print("Você pode acessar Redes Sociais sem supervisão!")  
else:
    print("Seus pais não deveriam você acessar Redes Sociais sem supervisão!")  

print(int("26"))

print(float("123.345"))
#print(float("123.3A45")) String com letras não pode ser convertida em número

print(str(14))

print(len([23,34,45,46]))

array = [1, 2, 3]
print(max(array))
print(min(array))

list1 = [16, 23, 44, 75]
print(sum(list1))

#Criando Funções Usando Outras Funções

import math

#Verificando se um número é primo

def numPrimo(num):
    if (num % 2) == 0 and num > 2: 
        return "Este número não é primo"
    for i in range(3, int(math.sqrt(num)) + 1, 2):
        if (num % i) == 0:
            return "Este número não é primo"
    return "Este número é primo"

numPrimo(541)

numPrimo(2)

caixa_baixa = "Este Texto Deveria Estar Todo Em LowerCase"

def lowercase(text):
    return text.lower()

lowercased_string = lowercase(caixa_baixa)

print(lowercased_string)

#Fazendo Split dos Dados

def split_string_palavras(text):
    return text.split(" ")

texto = "Esta função será bastante útil para separar grandes volumes de dados."

#Isso divide a string em uma lista de palavras
print(split_string_palavras(texto))

#Podemos atribuir o output de uma função para uma variável

token = split_string_palavras(texto)

print(token)

#Fazendo split dos dados

def split_string_letras(text):
    texto = text.upper()
    for letra in texto:
        print(letra)

split_string_letras(texto)