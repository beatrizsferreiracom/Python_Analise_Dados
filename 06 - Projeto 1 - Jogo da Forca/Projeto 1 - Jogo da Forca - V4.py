#Projeto 1 - Desenvolvimento de Game em Linguagem Python - Jogo da Forca - Versão 4

#Import
import random
from os import system, name

#Função para limpar a tela a cada execução
def limpa_tela():

    if name == 'nt':
        _ = system('cls')

#Função que desenha a forca na tela
def mostrar_forca(chances):

    #Lista de estágios da forca
    estagios = [  #estágio 6 (final)
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                """,
                #estágio 5
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / 
                   -
                """,
                #estágio 4
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |      
                   -
                """,
                #estágio 3
                """
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |     
                   -
                """,
                #estágio 2
                """
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                   -
                """,
                #estágio 1
                """
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                   -
                """,
                #estágio 0
                """
                   --------
                   |      |
                   |      
                   |    
                   |      
                   |     
                   -
                """
    ]
    return estagios[chances]

#Função do jogo
def game():

    limpa_tela()
    print("\nBem vindo ao jogo da forca!")
    print("Adivinhe a palavra abaixo:\n")
    
    #Bloco 'try-except' para abrir o arquivo de palavras e garantir que ele exista
    try:
        with open('arquivos/frutas.txt', 'r', encoding='utf8') as f:
            palavras = f.read().splitlines()
    except FileNotFoundError:
        print("Erro: O arquivo 'arquivos/frutas.txt' não foi encontrado.")
        print("Certifique-se de que o arquivo existe no diretório correto.")
        return #Encerra a função se o arquivo não for encontrado
    
    #Escolhe randomicamente uma palavra
    palavra = random.choice(palavras)
    
    #Lista  de letras  da palavra
    lista_letras_palavras = [letra for letra in palavra]
    
    #Cria o tabuleiro com o caracter "_" multiplicado pelo comprimento da palavra
    tabuleiro = ["_"] * len(palavra)
    
    #Número de chances
    chances = 6
    
    #Lista para as letras digitadas
    letras_tentativas = []
    
    #Loop enquanto número de chances for maior do que zero
    while chances > 0:
        
        print(mostrar_forca(chances))
        print("Palavra: ", tabuleiro)
        print("\n")
        
        #Tentativa
        tentativa = input("\nDigite uma letra: ")
        
        #Condicional para verificar se o usuário já tentou a letra anteriormente
        if tentativa in letras_tentativas:
            print("Você já tentou essa letra. Escolha outra!")
            continue
        elif len(tentativa) != 1: #Condicional para verificar se o usuário digitou mais de uma letra
            print("\nValor inválido! Digite apenas UMA letra.")
            continue
        elif not(tentativa.isalpha()): #Condicional para verificar se o usuário digitou uma letra
            print("\nVocê não digitou uma letra. Tente novamente.")
            continue
        
        #Lista de tentativas (letras)
        letras_tentativas.append(tentativa)      
            
        #Condicional para checar se a letra está na palavra
        if tentativa in lista_letras_palavras:
            
            print("Você acertou a letra!")
            
            #Loop
            for i in range(len(lista_letras_palavras)):

                #Condicional par atribuir a letra ao tabuleiro
                if lista_letras_palavras[i] == tentativa:
                    tabuleiro[i] = tentativa
            
            #Se todos os espaços foram preenchidos, o jogo acabou (vitória)
            if "_" not in tabuleiro:
                print("\nVocê venceu! A palavra era: {}".format(palavra))
                break
        else:
            print("Ops. Essa letra não está na palavra!")
            #Decremento
            chances -= 1
    
    #Condicional para verificar se as chances foram zeradas e o _ ainda existe no tabuleiro (derrota)
    if "_" in tabuleiro:
        print("\nVocê perdeu! A palavra era: {}.".format(palavra))

#Bloco main
if __name__ == "__main__":
    game()