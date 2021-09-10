"""
Reescreva a função leiaInt() que fizemos no exercício 104,
incluindo  agora a possibilidade da digitação de um número de tipo inválido.
Aproveite e crie também uma função leiaFloat() com a mesma funcionalidade.
"""


def leiaint(mensagem):
    while True:
        try:
            a = int(input(mensagem))
        except (ValueError, TypeError):
            print('\033[31mERRO! Digite um número inteiro válido.\033[m')
            continue
        except KeyboardInterrupt:
            print('\033[32mEntrada de dados interrompida pelo  usuário.\033[m')
            return 0
        else:
            return a


def leiafloat(mensagem):
    while True:
        try:
            a = float(input(mensagem))
        except (ValueError, TypeError):
            print('\033[31mERRO! Digite um número real válido.\033[m')
            continue
        except KeyboardInterrupt:
            print('\033[32mEntrada de dados interrompida pelo usuário.\033[m')
            return 0
        else:
            return a


# PROGRAMA PRINCIPAL
n1 = leiaint('Digite um número inteiro: ')
n2 = leiafloat('Digite um número real: ')
print(f'Você acabou de digitar o número inteiro {n1}')
print(f'Você acabou de digitar o número real {n2}')
