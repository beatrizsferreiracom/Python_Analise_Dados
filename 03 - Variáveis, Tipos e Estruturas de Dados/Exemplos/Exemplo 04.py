#Estruturas de Dados - Listas

#Trabalhando com Listas

#Criando uma lista
lista_1 = ["arroz, frango, tomate, leite"]

print(type(lista_1))

#Imprimindo a lista
print(lista_1)

#Criando outra lista
lista_2 = ["arroz", "frango", "tomate", "leite"]

print(type(lista_2))

#Imprimindo a lista
print(lista_2)

#Criando lista
lista_3 = [23, 100, "Cientista de Dados"]

print(type(lista_3))

#Imprimindo
print(lista_3)

#Atribuindo cada valor da lista a uma variável
item1 = lista_3[0]
item2 = lista_3[1]
item3 = lista_3[2]

#Imprimindo as variáveis
print(item1, item2, item3)

#Atualizando um item da lista
print(lista_2)

#Imprimindo um item da lista
print(lista_2[2])

#Atualizando um item da lista
lista_2[2] = "chocolate"

#Imprimindo a lista alterada
print(lista_2)

#Deletando um item da lista
print(lista_2)

#Não é possível deletar um item que não existe na lista. Vai gerar erro index out of range
#del lista_2[4]

#Deletando um item específico da lista
del lista_2[3]

#Imprimindo o item com a lista alterada
print(lista_2)

#Listas de Listas (Listas Alinhadas)

#Criando uma lista de listas
listas = [1, 2, 3], [10, 15, 14], [10.1, 8.7, 2.3]

#Imprimindo a lista
print(listas)

#Atribuindo um item da lista a uma variável
a = listas[0]

print(a)

b = a[0]

print(b)

list1 = listas[1]

print(list1)

valor_1_0 = list1[0]

print(valor_1_0)

#Operações com Listas

#Criando uma lista alinhada (lista de listas)
listas = [[1, 2, 3], [ 10, 15, 14], [10.2, 8,7, 2.3]]

print(listas)

#Atribuindo à variável ao primeiro valor da primeira lista
a = listas[0][0]
print(a)

b = listas[1][2]
print(b)

c = listas[0][2] + 10
print(c)

d = 10

e = d * listas[2][0]

#Concatenando Listas
lista_s1 = [34, 32, 56]

print(lista_s1)

lista_s2 = [21, 90, 51]

print(lista_s2)

#Concatenando listas
lista_total = lista_s1 + lista_s2

print(lista_total)

#Operador In

# Criando uma lista
lista_teste_op = [100, 2, 5, 3.4]

#Verificando se o valor 10 pertence a lista 
print(10 in lista_teste_op)

# Verificando se o valor 100 pertence a lista 
print(100 in lista_teste_op)

#Funções Built-In

#Criando uma lista
lista_numeros = [10, 20, 50, -3.4]

#Função len() retorna o comprimento da lista
print(len(lista_numeros))

# Função max() retorna o valor máximo da lista 
print(max (lista_numeros))

#Função min() retorna o valor mínimo da lista
print(min (lista_numeros))

#Criando uma lista
lista_formacoes_dsa = ["Analista de Dados", "Cientista de Dados", "Engenheiro de Dados"]

#Adicionando um item à lista
lista_formacoes_dsa.append("Engenheiro de IA")

print(lista_formacoes_dsa)

lista_formacoes_dsa.append("Engenheiro de IA")
print(lista_formacoes_dsa)

print(lista_formacoes_dsa.count("Engenheiro de IA"))

#Criando uma lista vazia

a = []

print(a)

type (a)

a.append(10)

print(a)

old_list = [1, 2, 5 , 10]

new_list = []

#Copiando os itens de uma lista para outra
for item in old_list:
    new_list.append(item)

print(new_list)

cidades = ['Recife', 'Manaus', 'Salvador'] 

cidades.extend(['Fortaleza', 'Palmas']) 

print(cidades)

print(cidades.index('Salvador'))

cidades.insert(2, 110)

print(cidades)

#Remove um item da lista 

cidades.remove(110)

print(cidades)

#Reverte a lista

cidades.reverse()

#Imprime a lista
print(cidades)

x = [3, 4, 2, 1]

print(x)

#Ordena a lista
x.sort()

print(x)