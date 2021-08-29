"""
Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços.
Ex:
APOS A SOPA
A SACADA DA CASA
A TORRE DA DERROTA
O LOBO AMA O BOLO
ANOTARAM A DATA DA MARATONA
"""
frase = 'A TORRE DA DERROTA'
lista = frase.split()
lista_sem_espaco = ''.join(lista)
contagem = 0
contador = len(lista_sem_espaco)
for i in range(0, len(lista_sem_espaco)):
    if lista_sem_espaco[i] == lista_sem_espaco[contador-1]:
        contador -= 1
        contagem += 1
if len(lista_sem_espaco) == contagem:
    print('É um palíndromo.')
else:
    print('Não é um palíndromo.')
