#Exercício 1 - Crie uma função que imprima a sequência de números pares entre 1 e 20 (a função não recebe parâmetro) 
#e depois faça uma chamada à função para listar os números

def pares():
    for i in range(2, 21, 2):
        print(i)

print(pares())