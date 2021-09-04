# EXERCÍCIO 53
"""
Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços.
Ex:
APOS A SOPA
A SACADA DA CASA
A TORRE DA DERROTA
O LOBO AMA O BOLO
ANOTARAM A DATA DA MARATONA
"""

# PROGRAMA PRINCIPAL
frase = str(input('Digite uma frase: '))   # Recebe frase
lista = frase.split()  # Transformando em lista só as palavras sem os espaços em branco
frase_sem_espacos = ''.join(lista)  # Juntando em uma string todas as palavras juntas
contagem = 0  # Variável recebe 0
contador = len(frase_sem_espacos)  # Variável contador recebe o n° de caracteres da frase_sem_espacos

for i in range(0, len(frase_sem_espacos)):  # Loop iterável de 0 até o tamanho da frase
    if frase_sem_espacos[i] == frase_sem_espacos[contador - 1]:  # SE a letra inicial for igual a do final
        contador -= 1  # Decremento do contador
        contagem += 1  # Incremento do contador

if len(frase_sem_espacos) == contagem:  # SE o numeros de letras for igual o valor da contagem
    print('É um palíndromo.')  # Imprime palíndromo

else:  # SENÃO
    print('Não é um palíndromo.')  # Imprime não palíndromo
