#Exercício 7 - Abaixo você encontra uma lista com temperaturas em graus Celsius
#Crie uma função anônima que converta cada temperatura para Fahrenheit
#Dica: para conseguir realizar este exercício, você deve criar sua função lambda, dentro de uma função 
#(que será estudada no próximo capítulo). Isso permite aplicar sua função a cada elemento da lista

Celsius = [39.2, 36.5, 37.3, 37.8]

Fahrenheit = map(lambda x: x * float(9 / 5) + 32, Celsius)

print (list(Fahrenheit))