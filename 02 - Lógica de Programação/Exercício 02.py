#Pseudocódigo - Calculadora Simples

#Inicie

    #Exiba "Bem-vindo à Calculadora"
    #Peça para o usuário inserir qual operação ele quer fazer (adição, subtração, multiplicação, divisão)
    #Peça para o usuário inserir o primeiro número
    #Armazene o primeiro número numa variável
    #Peça para o usuário inserir o segundo número
    #Armazene o segundo número numa variável
    #Calcule a operação escolhida pelo usuário entre os dois números:
        #Se a operação escolhida foi adição: numero 1 + numero 2
        #Se a operação escolhida foi subtração: numero 1 - numero 2
        #Se a operação escolhida foi multiplicação: numero 1 * numero 2
        #Se a operação escolhida foi divisão : numero 1 / numero 2
        #Se a operação escolhida for inválida exibir a mensagem "Operação inválida!"
    #Exiba o resultado

#Fim

print("Bem-vindo à Calculadora")

operacao = input("Escolha a operação ( + | - | * | / ): ")

num1 = float(input("\nDigite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

if operacao == '+':
    print("O resultado é: ", num1 + num2)
elif operacao == '-':
    print("O resultado é: ", num1 - num2)
elif operacao == '*':
    print("O resultado é: ", num1 * num2)
elif operacao == '/':
    print("O resultado é: ", num1 / num2)
else:
    print("Operação inválida!")