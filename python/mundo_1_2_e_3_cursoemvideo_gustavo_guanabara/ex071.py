"""
Crie um programa que simule o funcionamento de um caixa eletrônico.
No inicio, pergunte ao usuário qual será o valor a ser sacado (número inteiro) e o programa vai informar quantas cédulas de cada valor serão entregues.
OBS: Considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.
"""
saque = int(input('Digite o valor que deseja sacar: '))
notas_50 = saque // 50
notas_20 = (saque % 50) // 20
notas_10 = ((saque % 50) % 20) // 10
notas_1 = saque % 10
print(f'{"="*20}')
if notas_50 != 0:
    print(f'Notas de R$50:  {notas_50:>4}')
if notas_20 != 0:
    print(f'Notas de R$20:  {notas_20:>4}')
if notas_10 != 0:
    print(f'Notas de R$10:  {notas_10:>4}')
if notas_1 != 0:
    print(f'Notas de R$1 :  {notas_1:>4}')
print(f'{"="*20}')

# # Solução Guanabara:
# print('=' * 30)
# print('{:^30}'.format('BANCO CEV'))
# print('=' * 30)
# valor = int(input('Que valor você quer sacar? R$'))
# total = valor
# céd =  50
# totcéd = 0
# while True:
#     if total >= céd:
#         total -= céd
#         totcéd += 1
#     else:
#         if totcéd > 0:
#             print(f'Total de {totcéd} cédulas de RS{céd}')
#         if céd == 50:
#             céd = 20
#         elif céd == 20:
#             céd = 10
#         elif céd == 10:
#             céd = 1
#         totcéd = 0
#         if total == 0:
#             break
# print('=' * 30)
# print('Volte sempre ao BANCO CEV! Tenha um bom dia!')
