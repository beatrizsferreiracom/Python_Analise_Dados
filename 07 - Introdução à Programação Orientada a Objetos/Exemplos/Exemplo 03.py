#Trabalhando com Métodos de Classes em Python

#Criando uma classe chamada Circulo
class Circulo():

    #O valor pi é constante
    pi = 3.14

    #Quando um objeto desta classe for criado, este método será executado e o valor default do raio será 5
    def __init__(self, raio = 5):
        self.raio = raio

    #Este método calcula a área
    def area(self):
        return Circulo.pi * (self.raio ** 2)
    
    #Método para gerar um novo raio
    def setRaio(self, novo_raio):
        self.raio = novo_raio

    #Método para obter o raio do círculo
    def getRaio(self):
        return self.raio
    
#Criando o objeto circ, uma instância da classe Circulo()
circ = Circulo()

#Executando um método da classe Circulo
print(circ.getRaio())

#Criando outro objeto chamado circ1. Uma instância da classe Circulo()
#Agora sobrescrevendo o valor do atributo
circ1 = Circulo(7)

#Executando um método da classe Circulo
print(circ1.getRaio())

#Imprimindo o raio
print("O raio é:", circ.getRaio())

#Imprimindo a área
print("Área igual a:", circ.area())

#Gerando um novo valor para o raio do círculo
circ.setRaio(3)

#Imprimindo o novo raio
print("Novo raio igual a:", circ.getRaio())