"""
Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
Para salários superiores a R$1.250,00, calcule um aumento de 10%.
Para os inferiores ou iguais, o aumento é 15%.
"""
salario = float(input('Digite o salário do funcionário: '))
if salario > 1250:
    aumento = salario * 1.10
else:
    aumento = salario * 1.15
print(f'Seu salário era de R${salario:.2f} e foi para R${aumento:.2f}')

# # Solução Guanabara:
# salário = float(input('Qual é o salário do funcionário? R$'))
# if salário <= 1250:
#     novo = salário + (salário * 15 / 100)
# else:
#     novo = salário + (salário * 10 / 100)
# print('Quem ganhava R${:.2f} passa a ganhar R${:.2f} agora.'.format(salário, novo))
