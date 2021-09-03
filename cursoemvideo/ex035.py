# EXERCÍCIO 35
"""
Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.
"""

# PROGRAMA PRINCIPAL
reta_1 = float(input('Digite o primeiro valor: '))  # Recebendo valor da primeira reta
reta_2 = float(input('Digite o segundo valor: '))  # Recebendo valor da segunda reta
reta_3 = float(input('Digite o terceiro valor: '))  # Recebendo valor da terceira reta
if reta_1 > (reta_2 + reta_3) or reta_2 > (reta_1 + reta_3) or reta_3 > (reta_2 + reta_1):
    # ↑ SE a primeira reta for maior que a soma da segunda e da terceira reta
    # ↑↑ OU SE a segunda reta for maior que a soma da primeira e da terceira reta
    # ↑↑↑ OU SE a terceira reta for maior que a soma da segunda e da primeira reta
    print('Os valores informados não formam um triângulo.')  # Imprime na tela que não é um triângulo
else:  # SENÃO
    print('Os valores informados formam um triângulo.')  # Imprime na tela que é um triângulo

# # Solução Guanabara
# print('-='*20)
# print('Analisador de Triângulos')
# print('-+'*20)
# r1 = float(input('Primeiro segmento: '))
# r2 = float(input('Segundo segmento: '))
# r3 = float(input('Terceiro segmento: '))
# if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
#     print('Os segmentos acima PODEM FORMAR triângulo!')
# else:
#     print('Os segmentos acima NÃO PODEM FORMAR triângulo.')
