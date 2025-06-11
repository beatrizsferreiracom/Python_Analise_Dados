#Exercício 10 - Crie uma list comprehension que imprima os números menores que 5 em um intervalo de 1 a 10

numeros_menores_que_cinco = [x for x in range(11) if x < 5]

print(numeros_menores_que_cinco)