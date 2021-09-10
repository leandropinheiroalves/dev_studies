"""
Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.
"""
salario = float(input('Digite o valor do salário do funcionário: '))
aumento = salario * 0.15
salario_com_aumento = salario + aumento
print(f'O seu salário com aumento é R${salario_com_aumento}, você teve um aumento de R${aumento}.')
