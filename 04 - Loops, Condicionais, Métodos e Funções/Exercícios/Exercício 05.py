#Exercício 4 - Crie uma função que receba um argumento formal e uma possível lista de elementos. Faça duas chamadas 
#à função, com apenas 1 elemento e na segunda chamada com 4 elementos

def printArg(arg, *lista):
    print(arg)
    for i in lista:
        print(i)
    return

print(printArg('Arroz'))

print(printArg('Arroz', 'Feijão', 'Café', 'Açúcar'))