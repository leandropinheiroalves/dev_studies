"""
Faça um programa que leia uma frase pelo teclado e mostre:
    * Quantas vezes aparece a letra "A".
    * Em que posição ela aparece a primeira vez.
    * Em que posição ela aparece a última vez.
"""
frase = str(input('Digite uma frase: ')).strip().upper()
print(f'A letra A aparece {frase.count("A")} vezes')
print(f'A letra A aparece pela primeira vez na posição {frase.find("A") + 1}')
print(f'A letra A aparece pela última vez na posição {frase.rfind("A") + 1}')

# Solução Guanabara:
# frase = str(input('Digite uma frase: ')).upper().strip()
# print('A letra A aparece {} vezes na frase.'.format(frase.count('A')))
# print('A primeira letra A apareceu na posição {}.'.format(frase.find('A')+1))
# print('A última letra A apareceu na posição {}.'.format(frase.rfind('A')+1))
