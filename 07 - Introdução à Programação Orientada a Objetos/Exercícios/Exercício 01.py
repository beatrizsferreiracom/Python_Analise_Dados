#Lab 4 - Hangman Game (Jogo da Forca) - Programação Orientada a Objetos

#Import
import random
from os import system, name

#Função para limpar a tela a cada execução
def limpa_tela():

    if name == 'nt':
       _ = system('cls')

#Board (tabuleiro)
board = ['''

>>>>>>>>>>Hangman<<<<<<<<<<

+---+
|   |
    |
    |
    |
    |
=========''', '''

+---+
|   |
O   |
    |
    |
    |
=========''', '''

+---+
|   |
O   |
|   |
    |
    |
=========''', '''

 +---+
 |   |
 O   |
/|   |
     |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
     |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
/    |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
/ \  |
     |
=========''']


#Classe
class Hangman:

	#Método Construtor
    def __init__(self, palavra):
        self.palavra = palavra
        self.letras_descobertas = ['_' for letra in self.palavra]
        self.letras_erradas = []
        self.letras_tentadas = []
        self.chances = 6
        
	#Método para adivinhar a letra
    def adivinhar(self, letra):
        
        self.letras_tentadas.append(letra)

        if letra in self.letras_descobertas or letra in self.letras_erradas:
            return

        acertou = False
        if letra in self.palavra:
            for i, char in enumerate(self.palavra):
                if char == letra:
                    self.letras_descobertas[i] = letra
            acertou = True
        else:
            if letra not in self.letras_erradas:
                self.letras_erradas.append(letra)
                self.chances -= 1
            return False
	
	#Método para verificar se o jogo terminou
    def fim_de_jogo(self):
        return self.vitoria() or (self.chances == 0)
		
	#Método para verificar se o jogador venceu
    def vitoria(self):
        return '_' not in self.letras_descobertas
		
	#Método para não mostrar a letra no board
    def esconder_palavra(self):
        return " ".join(self.letras_descobertas)
		
	#Método para checar o status do game e imprimir o board na tela
    def checar_status(self):
        print(board[6 - self.chances])
        print("\nPalavra:", self.esconder_palavra())
        print("Chances restantes:", self.chances)
        print("Letras erradas:", " ".join(self.letras_erradas))
        print("Letras tentadas:", " ".join(self.letras_tentadas))

# Função para ler uma palavra de forma aleatória do banco de palavras
def palavra_aleatoria():

    #Bloco 'try-except' para abrir o arquivo de palavras e garantir que ele exista
    try:
        with open('arquivos/frutas.txt', 'r', encoding='utf8') as f:
            palavras = f.read().splitlines()
        return random.choice(palavras)
    except FileNotFoundError:
        print("Erro: O arquivo 'arquivos/frutas.txt' não foi encontrado.")
        print("Crie o arquivo e a pasta 'arquivos' ou mude o caminho no código.")
        exit() #Encerra o programa se o arquivo não for encontrado

#Bloco main | Chamada da função do game (Execução)
def main():

    #Limpa a tela
    limpa_tela()

    #Cria o objeto do jogo
    palavra = palavra_aleatoria()
    game = Hangman(palavra)

    letras_tentadas = []

    print("\nBem-vindo ao jogo da forca!")
    print("Adivinhe a palavra abaixo:\n")

    #Enquanto o jogo não tiver terminado, print do status, solicita uma letra e faz a leitura
    while not game.fim_de_jogo():

        #Mostra o status do jogo
        game.checar_status()

        #Loop para verificar e validar a tentativa
        while True:

            tentativa = input("\nDigite uma letra: ").lower()

            if len(tentativa) != 1:
                print("\nValor inválido! Digite apenas UMA letra.")
            elif not tentativa.isalpha():
                print("\nVocê não digitou uma letra. Tente novamente.")
            elif tentativa in game.letras_tentadas:
                print("\nOpa! Você já tentou essa letra antes.")
            else:
                break
        
        #Limpa a tela para a próxima rodada
        limpa_tela()

        #Passa a letra para o método de adivinhação
        game.adivinhar(tentativa)

    #Verifica o status final do jogo
    game.checar_status()

    #Imprime a mensagem final
    if game.vitoria():
        print("\nParabéns! Você venceu! A palavra era:", game.palavra)
    else:
        print("\nGame over! Você perdeu. A palavra era:", game.palavra)

# Executa o programa
if __name__ == "__main__":
    main()