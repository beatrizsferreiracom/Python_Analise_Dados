#Exercício 6 - Execute o código abaixo e certifique-se que compreende a diferença entre variável global e local

total = 0

def soma(arg1, arg2):
    total = arg1 + arg2; 
    print ("Dentro da função o total é: ", total)
    return total;

soma(10, 20);

print ("Fora da função o total é: ", total)

#A variável total fora da função tem o valor atribuído a ela e se mantém a mesma caso não haja uma nova atribuição ou modificação direta

#A variável total dentro da função é definida de acordo com o valor informado na hora da chamada, e segue as condições estabelecidas dentro dela