#Exercício 3 - Crie uma função que receba como parâmetro uma lista de 4 elementos, adicione 2 elementos a lista e 
#imprima a lista

def novaLista(lista):
    lista.append('Sal')
    lista.append('Óleo')
    return

lista = ['Arroz', 'Feijão', 'Café', 'Açúcar']

novaLista(lista)

print(lista)