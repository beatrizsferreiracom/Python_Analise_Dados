#Projeto 1 - Desenvolvimento de um Game em Linguagem Python - Jogo da Forca - Versão 1

#Import
import random
from os import system, name

#Função para limpar a tela a cada execução
def limpa_tela():

    if name == 'nt':
       _ = system('cls')

#Função do Game
def game():

    #Chamada da função de limpeza
    limpa_tela()

    print("\nBem-vindo ao jogo da forca!")
    print("\nAdivinhe a palavra abaixo:\n")

    #Lista de palavras para o jogo
    palavras = ['banana', 'abacate', 'uva', 'morango', 'laranja']

    #Função random para escolher um palavra aleatória
    palavra = random.choice(palavras)

    #List comprehension para as letras da palavra
    letras_descobertas = ['_' for letra in palavra]

    #Número de chances
    chances = 6

    #Lista para as letras erradas
    letras_erradas = []

    #Loop para número de chances > 0
    while chances > 0:

        print(" ".join(letras_descobertas))
        print("\nChances restantes:", chances)
        print("Letras erradas:", " ".join(letras_erradas))

        #Variável da tentativa
        tentativa = input("\nDigite uma letra: ").lower()

        #Condicional para checar se a letra está na palavra
        if tentativa in palavra:
            i = 0
            for letra in palavra:
                if tentativa == letra:
                    letras_descobertas[i] = letra
                i += 1
        else:
            chances -= 1
            letras_erradas.append(tentativa)
            print("\nLetra incorreta. Tentativas restantes:", chances)  

        #Condicional para verificar se todas as letras foram descobertas (vitória)
        if "_" not in letras_descobertas:
            print("\nVocê venceu! A palavra era:", palavra)
            break
    
    #Condicional para verificar se as chances foram zeradas (derrota)
    if chances == 0:
        print("\nVocê perdeu! A palavra era:", palavra)

#Bloco main | Chamada da função do game (Execução)
if __name__ == "__main__":
    game()