#Exercícios - Loops, Condicionais, Métodos e Funções

#Exercício 1 - Crie uma estrutura que pergunte ao usuário qual o dia da semana. Se o dia for igual a Domingo ou 
#igual a sábado, imprima na tela "Hoje é dia de descanso", caso contrário imprima na tela "Você precisa trabalhar!"

dia = input("Que dia da semana é hoje? ")

if dia == 'Domingo' or dia == 'Sábado':
    print("Hoje é dia de descanso")
else:
    print("Você precisa trabalhar!")