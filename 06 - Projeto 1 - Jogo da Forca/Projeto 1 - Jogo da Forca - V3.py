#Projeto 1 - Desenvolvimento de um Game em Linguagem Python - Jogo da Forca - Versão 3

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

    #Bloco 'try-except' para abrir o arquivo de palavras e garantir que ele exista
    try:
        with open('arquivos/frutas.txt', 'r', encoding='utf8') as f:
            palavras = f.read().splitlines()
    except FileNotFoundError:
        print("Erro: O arquivo 'arquivos/frutas.txt' não foi encontrado.")
        print("Certifique-se de que o arquivo existe no diretório correto.")
        return #Encerra a função se o arquivo não for encontrado

    #Função random para escolher um palavra aleatória
    palavra = random.choice(palavras)

    #List comprehension para as letras da palavra
    letras_descobertas = ['_' for letra in palavra]

    #Número de chances
    chances = 6

    #Lista para as letras erradas
    letras_erradas = []

    #Lista para as letras que já foram tentadas
    letras_tentadas = []

    #Loop para o jogo executar, equanto o número de chances > 0
    while chances > 0:

        print(" ".join(letras_descobertas))
        print("\nChances restantes:", chances)
        print("Letras erradas:", " ".join(letras_erradas))

        #Loop para verificar e validar a tentativa
        while True:
            tentativa = input("\nDigite uma letra: ").lower()

            if len(tentativa) != 1: #Condicional para verificar se foi digitada mais de uma letra
                print("\nValor inválido! Digite apenas UMA letra.")
            elif not(tentativa.isalpha()): #Condicional para verificar se o usuário digitou uma letra
                print("\nVocê não digitou uma letra. Tente novamente.")
            elif tentativa in letras_tentadas: #Condicional para verificar se o usuário já tentou a letra anteriormente
                print("\nOpa! Você já tentou essa letra antes.")
            else: #Condicional para adicionar a letra a lista de letras tentadas, após passar de todas as outras verificações
                letras_tentadas.append(tentativa)
                break

        if tentativa in palavra:
            for i, letra in enumerate(palavra): #Usando enumerate para obter o índice e a letra corretamente
                if tentativa == letra:
                    letras_descobertas[i] = letra
                i += 1
        else:
            chances -= 1
            letras_erradas.append(tentativa)

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