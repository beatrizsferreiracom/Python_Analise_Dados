#Funções Built-in

#Função Map

#Função Python que retorna um número ao quadrado
def potencia(x):
    return x ** 2

numeros = [1, 2, 3, 4, 5]

numeros_ao_quadrado = list(map(potencia, numeros))

print(numeros_ao_quadrado)

#Criando duas funções

#Função 1 - Recebe uma temperatura como parâmetro e retorna a temperatura em Farenheit
def farenheit(T):
    return(float(9) / 5 * T + 32)

#Função 2 - Recebe uma temperatura como parâmetro e retorna a temperatura em Celsius
def celsius(T):
    return(float(5) / 9 * (T - 32))

#Criando uma lista
temperaturas = [0, 22.5, 40, 100]

#Aplicando a função a cada elemento da lista de temperaturas.
#Em Python 3, a função map() retorna um iterator
print(map(farenheit, temperaturas))

#Função map() retornando a lista de temperaturas convertidas em Fahrenheit
print(list(map(farenheit, temperaturas)))

#Usando um loop for para imprimir o resultado da função map()
for temp in map(farenheit, temperaturas):
    print(temp)

#Convertendo para Celsius
print(map(celsius, temperaturas))

print(list(map(celsius, temperaturas)))

#Usando expressão lambda
print(map(lambda x: (5.0 / 9) * (x - 32), temperaturas))

print(list(map(lambda x: (5.0 / 9) * (x - 32), temperaturas)))

#Somando os elementos de 2 listas
a = [1, 2, 3, 4]
b = [5, 6, 7, 8]

print(list(map(lambda x, y : x + y, a, b)))

#Somando os elementos de 3 listas
a = [1, 2, 3, 4]
b = [5, 6, 7, 8]
c = [9, 10, 11, 12]

print(list(map(lambda x, y, z: x + y + z, a, b, c)))