#Métodos

#Tudo em Python é objeto. E cada objeto tem métodos e atributos.

#Atributos são propriedades, características do objeto.
#Métodos são funções com ações que podem ser executadas nos objetos.

#Criando uma lista
lista = [100, -2, 12, 65, 0]
type(lista)

#Verificando métodos e atributos
print(lista)

#Usando um método do objeto lista
lista.append(100)

#Imprimindo a lista
print(lista)

#Usando um método do objeto lista
lista.count(100)

#A função help() explica como utilizar cada método de um objeto
help(lista.count)

#A função dir() mostra todos os métodos e atributos de um objeto
dir(lista)

#Criando uma string
frase = 'Isso é uma string'
type(frase)

#Verificando métodos e atributos
print(frase)

#O método de um objeto pode ser chamado dentro de uma função, como print()
print (frase.split())