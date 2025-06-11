#Exercício 2 - Crie uma lista de 5 frutas e verifique se a fruta 'Morango' faz parte da lista

lista = ['Abacaxi', 'Morango', 'Banana', 'Maracujá', 'Laranja']

for i in lista:
    if i == 'Morango':
        print("Morango está na lista de frutas")
    else:
        print("Morango não está na lista de frutas")
        break