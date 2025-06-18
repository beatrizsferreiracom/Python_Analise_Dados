#Exercício 3 - Crie a classe Smartphone com 2 atributos, tamanho e interface e crie a classe MP3Player com os 
#atributos capacidade. A classe MP3player deve herdar os atributos da classe Smartphone.

class Smartphone():

    def __init__(self, tamanho, interface):
        self.tamanho = tamanho
        self.interface = interface
        print("Dispositivo criado.")

class MP3Player(Smartphone):

    def __init__(self, capacidade, tamanho = 'Pequeno', interface = 'Led'):
        self.capacidade = capacidade
        Smartphone.__init__(self, tamanho, interface)

    def imprimir_dados(self):
        print("Dados do dispositivo:")
        print("Tamanho:", self.tamanho)
        print("Interface:", self.interface)
        print("Capacidade:", self.capacidade)

dispositivo1 = MP3Player("32 GB")

dispositivo1.imprimir_dados()