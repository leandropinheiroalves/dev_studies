"""
Crie um programa que tenha a função leiaInt(), que vai funcionar de forma semelhante á função input() do Python,
só que fazendo a validação para aceitar apenas um valor numérico.
Ex:
n = leiaInt('Digite um n')
"""


def leiaInt(mensagem):
    a = input(mensagem)
    while not a.isnumeric():
        print('\033[31mERRO! Digite um número inteiro válido.\033[m')
        a = input(mensagem)
    return a


# PROGRAMA PRINCIPAL
n = leiaInt('Digite um número: ')
print(f'Você acabou de digitar o número {n}')
