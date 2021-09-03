# EXERCÍCIO 32
"""
Faça um programa que leia um ano qualquer e mostre se ele é BISSEXTO.
"""

# PROGRAMA PRINCIPAL
ano = int(input('Digite um ano: '))  # Recebendo ano
if ano % 4 == 0:  # SE o resto da divisão do ano por 4 for zero
    if ano % 100 == 0:  # SE o resto da divisão do ano por 100 for zero
        if ano % 400 == 0:  # SE o resto da divisão do ano por 400 for zero
            print('O ano informado É BISSEXTO!')  # Imprime na tela que o ano é bissexto
        else:  # SENÃO
            print('O ano informado NÃO É BISSEXTO!')  # Imprime na tela que o ano não é bissexto
    else:  # SENÃO
        print('O ano informado É BISSEXTO!')  # Imprime na tela que o ano é bissexto
else:  # SENÃO
    print('O ano informado NÃO É BISSEXTO!')  # Imprime na tela que o ano não é bissexto

# Solução Guanabara:
# from datetime import date
# ano = int(input('Que ano quer analisar? Coloque 0 para analisar o ano atual: '))
# if ano == 0:
#     ano = date.today().year
# if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
#     print('O ano {} é BISSEXTO'.format(ano))
# else:
#     print('O ano {} NÃO é BISSEXTO'.format(ano))
