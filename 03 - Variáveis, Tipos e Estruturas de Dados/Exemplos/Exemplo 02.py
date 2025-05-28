#Trabalhando com Variáveis

#Atribuindo o valor 1 à variável var_teste
var_teste = 1

#Imprimindo o valor da variável
print(var_teste)

#Substituindo o valor da variável
var_teste = 2
print(var_teste)

#Tipo da variável
print(type(var_teste))

#Sustituindo o valor e tipo
var_teste = 9.5
print(var_teste)
print(type(var_teste))

#Variáveis podem ter "vários" nomes
x = 1
print(x)

#Declaração Múltipla
pessoa1, pessoa2, pessoa3 = "Bob", "Maria", "Ana"

print(pessoa1)
print(pessoa2)
print(pessoa3)

#Atribuindo valor de uma variável a partir de outra
fruta1 = fruta2 = fruta3 = 'Melancia'

print(fruta1)
print(fruta2)
print(fruta3)

#Variáveis atribuídas a Outras Variáveis e Ordem dos Operadores

largura = 2
altura = 4

area = largura * altura

print("Área =", area)

perimetro = 2 * largura + 2 * altura

print("Perímetro =", perimetro)

#A ordem dos operadores é a mesma seguida na Matemática
perimetro = 2 * (largura + 2) * altura

print("Perímetro =", perimetro)

#Operações com Variáveis

idade1 = 25
idade2 = 35

print(idade1 + idade2)
print(idade1 - idade2)
print(idade1 * idade2)
print(idade1 / idade2)
print(idade1 % idade2)

#Concatenação de Variáveis

nome = "Bob"
sobrenome = "Marley"

fullName = nome + " " + sobrenome

print(fullName)