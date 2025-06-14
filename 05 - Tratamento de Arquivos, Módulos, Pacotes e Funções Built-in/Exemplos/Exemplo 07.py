#Tratamento de Erros e Excessões

#Erro de sintaxe
#print('Hello) - Faltou a aspa de fechamento

#Erro de tipo
#8 + s - Não é possível somar tipo string

#Criando um função
def numDiv(num1, num2):
    resultado = num1 / num2
    print(resultado)

#Execução não gera erro
print(numDiv(4, 2))

#Execução gerando erro
#numDiv(4, 0) - Não é possível dividir por 0

#Try, Except, Finally

try: 
    8 + 's'
except TypeError:
    print("Operação não permitida")

#Utilizando try, except e else
try:
    f = open('arquivos/testandoerros.txt', 'w')
    f.write('Gravando no arquivo')
except IOError:
    print("Erro: Arquivo não encontrado ou não pode ser salvo.")
else:
    print("Conteúdo gravado com sucesso!")
    f.close()

#Utilizando try, except e else
try:
    f = open('arquivos/testandoerros', 'r')
except IOError:
    print("Erro: Arquivo não encontrado ou não pode ser lido.")
else:
    print("Conteúdo gravado com sucesso!")
    f.close()

#Utilizando try, except, else e finally
try:
    f = open('arquivos/testandoerros.txt', 'w')
    f.write('Gravando no arquivo')
except IOError:
    print("Erro: Arquivo não encontrado ou não pode ser salvo.")
else:
    print("Conteúdo gravado com sucesso!")
    f.close()
finally:
    print("Comandos no bloco finally são sempre executados!")

#Cada possibilidade de erro deve ser tratada no seu próprio programa.
def askint():
    try:
        val = int(input("Digite um número: "))
    except:
        print("Você não digitou um número!")
    finally:
        print("Obrigado!")

print(askint())

#Digitar novamente
def askint():
    try:
        val = int(input("Digite um número: "))
    except:
        print("Você não digitou um número!")
        val = int(input("Tente novamente. Digite um número: "))
    finally:
        print("Obrigado!")
    print(val)

print(askint())

#Digitar novamente até ser um número
def askint():
    while True:
        try:
            val = int(input("Digite um número: "))
        except:
            print("Você não digitou um número!")
            continue
        else:
            print("Obrigado por digitar um número!")
            break
        finally:
            print("Fim da execução!")
        print(val)

print(askint())