#Programação Orientada a Objetos

#Classes

class Livro():

    #Este método vai inicializar cada objeto criado a partir desta classe
    #O nome deste  método é __init__
    #(self) é uma referência a cada atributo da própria classe (e não de uma classe mãe, por exemplo)

    def __init__(self):

        #Atributos são propriedades
        self.titulo = 'Sapiens = Uma Breve História da Humanidade'
        self.isbn = 9988888
        print("Construtor chamado para criar um objeto desta classe.")

    #Métodos são funções que executam ações nos objetos da classe
    def imprime(self):
        print("Foi criado o livro %s com ISBN %d" %(self.titulo, self.isbn))

#Criando uma instância da classe livro
Livro1 = Livro()

#O objeto Livro1 é do tipo Livro
print(type(Livro1))

#Atributo do objeto Livro1
print(Livro1.titulo)

#Método do objeto Livro1
Livro1.imprime()

#Criando a classe Livro com parâmetros no método construtor
class Livro():

    def __init__(self, titulo, isbn):
        self.titulo = titulo
        self.isbn = isbn
        print("Construtor chamado para criar objeto desta classe.")

    def imprime(self, titulo, isbn):
        print("Este é o livro %s e ISBN %d" %(titulo, isbn))

Livro2 = Livro("O Poder do Hábito", 77886611)

print(Livro2.titulo)

#Método do objeto Livro2
Livro2.imprime("O Poder do Hábito", 77886611)

#Criando a classe
class Algoritmo():

    def __init__(self, tipo_algo):
        self.tipo = tipo_algo
        print("Construtor chamado para criar um objeto desta classe.")
    
#Criando um objeto a partir da classe
algo1 = Algoritmo(tipo_algo = 'Random Forest')

#Criando um objeto a partir da classe
algo2 = Algoritmo(tipo_algo = 'Deep Learning')

#Atributo da classe
print(algo1.tipo)

#Atributo da classe
print(algo2.tipo)