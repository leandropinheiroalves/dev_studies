# Hangman Game (Jogo da Forca) 
# Programação Orientada a Objetos

# Import
import random

# Board (tabuleiro)
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


# Classe
class Hangman:

      
   
    # Método Construtor
    def __init__(self, word):
        self.word = word
        print(board[0])

    erros = 0
    # Método para adivinhar a letra
    def guess(self, letter):
        lista1 = list('_' * len(letter))
        lista2 = list()
        for i, l in enumerate(letter):
            if letter == self.word[i]:
                lista1[i] = l
        if letter in self.word:
            print('Acertou.')
        else:
            print('Errou')
            erros += 1
        if erros > 6:
            print('Você Perdeu! O jogo acabou porque você teve mais do que 6 erros.')

    # Método para verificar se o jogo terminou
    def hangman_over(self):
		if self.word


    # Método para verificar se o jogador venceu
    def hangman_won(self):


    # Método para não mostrar a letra no board
    def hide_word(self):


    # Método para checar o status do game e imprimir o board na tela
    def print_game_status(self):


# Função para ler uma palavra de forma aleatória do banco de palavras
def rand_word():
    with open("palavras.txt", "rt") as f:
        bank = f.readlines()
    return bank[random.randint(0, len(bank))].strip()


# Função Main - Execução do Programa
def main():

    # Objeto
    game = Hangman(rand_word())

    # Enquanto o jogo não tiver terminado, print do status, solicita uma letra e faz a leitura do caracter


    # Verifica o status do jogo
    game.print_game_status()

    # De acordo com o status, imprime mensagem na tela para o usuário
    if game.hangman_won():
        print('\nParabéns! Você venceu!!')
    else:
        print('\nGame over! Você perdeu.')
        print('A palavra era ' + game.word)

    print('\nFoi bom jogar com você! Agora vá estudar!\n')

# Executa o programa		
if __name__ == "__main__":
    main()
print('agua')
