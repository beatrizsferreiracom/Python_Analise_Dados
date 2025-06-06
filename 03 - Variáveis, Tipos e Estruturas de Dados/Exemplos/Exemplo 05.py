#Dicionários

#Trabalhando com Dicionários

#Isso é uma lista
estudantes_lst = ["Pedro", 24, "Ana", 22, "Ronaldo", 26, "Janaina", 25]

print(estudantes_lst)

print(type(estudantes_lst))

#Isso é um dicionário
estudantes_dict = {"Pedro":24, "Ana":22, "Ronaldo":26, "Janaina":25}

print(estudantes_dict)

print(type(estudantes_dict))

#Consulta de dados
print(estudantes_dict["Pedro"])

estudantes_dict["Marcelo"] = 23

print(estudantes_dict["Marcelo"])

#Limpando o dicionário
estudantes_dict.clear()

print(estudantes_dict)

#Deletando o dicionário
del estudantes_dict

estudantes = {"Pedro":24, "Ana":22, "Ronaldo":26, "Janaina":25}

print(estudantes)

print(len(estudantes))

print(estudantes.keys())
print(estudantes.values())
print(estudantes.items())

#Atualizando o dicionário
estudantes2 = {"Camila":27, "Adriana":28, "Roberta":26}
print(estudantes2)

estudantes2.update(estudantes2)
print(estudantes)

dict1 = {}

dict1["key1"] = "Data Science"
dict1["key2"] = 10
dict1["key3"] = 100

print(dict1)

a = dict1["key1"]
b = dict1["key2"]
c = dict1["key3"]

print(a, b, c)

# Dicionário de listas
dict2 = {'chavel':1230, 'chave2':[22, 453, 73.4], 'chave3':['picanha', 'fraldinha', 'alcatra']}

print(dict2)

print(dict2['chave2'])

#Acessando um item da lista, dentro do dicionário 
print(dict2['chave3'][0].upper())

#Operações com itens da lista, dentro do dicionário varl = dict2['chave2'][0] - 2

varl = dict2['chave2'][0] - 2

print(varl)

#Duas operações no mesmo comando, para atualizar um item dentro da lista
dict2['chave2'][0] -= 2

print(dict2)

#Criando Dicionários Aninhados

dict_aninhado = {'key1':{'key2_aninhada':{'key3_aninhada':'Dict aninhado em Python'}}}

print(dict_aninhado['key1']['key2_aninhada']["key3_aninhada"])