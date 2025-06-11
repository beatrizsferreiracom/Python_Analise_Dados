#Calculadora em Python

#Desenvolva uma calculadora em Python com tudo que você aprendeu nos capítulos até aqui no curso.

def soma(x, y):
    return x + y

def subtracao(x, y):
    return x - y

def multiplicacao(x, y):
    return x * y

def divisao(x, y):
    return x / y

print("\n******************* Calculadora em Python *******************")

print("\nSelecione o número da operação desejada:\n")

print("1 - Soma")
print("2 - Subtração")
print("3 - Multiplicação")
print("4 - Divisão")

op = int(input("\nDigite sua opção (1/2/3/4): "))

x = int(input("\nDigite o primeiro número: "))
y = int(input("\nDigite o segundo número: "))

if op == 1:
    print(f"\n{x} + {y} =", soma(x, y))
elif op == 2:
    print(f"\n{x} - {y} =", subtracao(x, y))
elif op == 3:
    multiplicacao(x, y)
    print(f"\n{x} * {y} =", multiplicacao(x, y))
elif op == 4:
    divisao(x, y)
    print(f"\n{x} / {y} =", divisao(x, y))
else: 
    print("\nOpção inválida!")