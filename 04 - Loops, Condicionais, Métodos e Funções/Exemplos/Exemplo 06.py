#Expressão Lambda

#Definindo uma função - 3 linhas de código

def potencia(num):
    resultado = num ** 2
    return resultado

print(potencia(5))

#Definindo uma função - 2 linhas de código

def potencia(num):
    return num ** 2

print(potencia(5))

#Definindo uma função - 1 linha de código

def potencia(num): return num ** 2

print(potencia(5))

#Definindo uma expressão lambda (função anônima)

potencia = lambda num: num ** 2

print(potencia(5))

#Lembre: operadores de comparação retornam boolean: true or false

Par = lambda x: x % 2 == 0
print(Par(3))
print(Par(4))

first = lambda s: s[0]
print(first('Python'))

reverso = lambda s: s[::-1]
print(reverso('Python'))

addNum = lambda x, y : x + y
print(addNum(2, 3))