"""
Faça um mini-sistema que utilize o interactive help do Python.
O usuário vai digitar o comando e o manual vai aparecer.
Quando o usuário digitar a palavra 'FIM', o programa se encerrará.
OBS: use cores.
"""


# def pyhelp():
#     comando = ''
#     while comando != 'fim':
#         print('\033[31;40m=' * 30)
#         print(f'{"SISTEMA DE AJUDA PyHELP":^30}')
#         print('=' * 30)
#         comando = input('\033[mFunção ou Biblioteca > ')
#         print(f'\033[30;45m→Acessando o manual do comando "{comando}":')
#         help(comando)
#
# pyhelp()

# Solução Guanabara:
from time import sleep
c = ('\033[m',          # 0 - sem cor
     '\033[0;30;41m',   # 1 - vermelhor
     '\033[0;30;42m',   # 2 - verde
     '\033[0;30;43m',   # 3 - amarelo
     '\033[0;30;44m',   # 4 - azul
     '\033[0;30;45m',   # 5 - roxo
     '\033[7;30m',      # 6 - branco
     )


def ajuda(com):
    título(f'Acessando o manual do comando "{com}"', 4)
    print(c[3], end='')
    help(com)
    print(c[0], end='')
    sleep(2)


def título(msg, cor=0):
    tam = len(msg) + 4
    print(c[cor], end='')
    print('=' * tam)
    print(f'  {msg}')
    print('=' * tam)
    print(c[0], end='')
    sleep(1)


# Programa Principal
comando = ''
while True:
    título('SITEMA DE AJUDA PyHELP', 2)
    comando = str(input('Função ou Biblioteca > '))
    if comando.upper() == 'FIM':
        break
    else:
        ajuda(comando)
título('ATÉ LOGO!', 1)
