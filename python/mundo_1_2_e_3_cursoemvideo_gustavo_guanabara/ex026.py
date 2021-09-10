"""
Faça um programa que leia uma frase pelo teclado e mostre:
    * Quantas vezes aparece a letra "A".
    * Em que posição ela aparece a primeira vez.
    * Em que posição ela aparece a última vez.
"""
frase = str(input('Digite uma frase: ')).strip().upper()
# Recebendo uma frase, removendo os espaços do inicio, do fim e transformando em maiúsculas

print(f'A letra A aparece {frase.count("A")} vezes')
# Contando e retornando quantos vezes aparece a letra 'A'

print(f'A letra A aparece pela primeira vez na posição {frase.find("A") + 1}')
# Identificando e retornando a posição em que a letra 'A' aparece pela primeira vez

print(f'A letra A aparece pela última vez na posição {frase.rfind("A") + 1}')
# Identificando e retornando a posição em que a letra 'A' aparece pela última vez

# Solução Guanabara:
# frase = str(input('Digite uma frase: ')).upper().strip()
# print('A letra A aparece {} vezes na frase.'.format(frase.count('A')))
# print('A primeira letra A apareceu na posição {}.'.format(frase.find('A')+1))
# print('A última letra A apareceu na posição {}.'.format(frase.rfind('A')+1))
