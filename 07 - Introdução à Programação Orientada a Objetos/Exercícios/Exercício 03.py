#Exercício 2 - Crie uma classe chamada Pessoa() com os atributos: nome, cidade, telefone e e-mail. Use pelo menos 2
#métodos especiais na sua classe. Crie um objeto da sua classe e faça uma chamada a pelo menos um dos seus métodos
#especiais.

class Pessoa():

    def __init__(self, nome, cidade, telefone, email):
        self.nome = nome
        self.cidade = cidade
        self.telefone = telefone
        self.email = email
        print("A pessoa foi cadastrada.")

    def imprimir_dados(self):
        print("\nPessoa cadastrada:")
        print("Nome:", self.nome)
        print("Cidade:", self.cidade)
        print("Telefone:", self.telefone)
        print("E-mail:", self.email)

    def imprimir_contato(self):
        print("\nDados de contato:")
        print("Telefone:", self.telefone)
        print("E-mail:", self.email)

pessoa1 = Pessoa("Livia Soares", "São Paulo", "11 1234-5678", "liviasoares@gmail.com")
pessoa2 = Pessoa("Carlos Machado", "Rio de Janeiro", "21 8765-4321", "carlosmachado@gmail.com")

pessoa1.imprimir_dados()
pessoa1.imprimir_contato()

pessoa2.imprimir_dados()
pessoa2.imprimir_contato()