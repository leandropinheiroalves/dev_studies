"""
Crie um programa que tenha uma tupla totalmente preenchida com uma contagem por extenso, de zero até vinte.
Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrálo por extenso.
"""
listagem = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze',
           'doze', 'treze', 'catorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
numero = int(input('Digite um número entre 0 e 20: '))
while True:
    if numero not in range(0, 21):
        numero = int(input('Número inválido. Digite um número entre 0 e 20: '))
    else:
        print(f'O número digitado foi {listagem[numero].upper()}.')
        break
