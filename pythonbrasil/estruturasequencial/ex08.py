"""Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês.
Calcule e mostre o total do seu salário no referido mês."""

valor_ganho_por_hora = float(input('Informe o valor ganho por hora trabalhada: '))
horas_trabalhadas = float(input('Informe o numero de horas trabalhada no mês: '))
salario = valor_ganho_por_hora * horas_trabalhadas

print(f'Horas trabalhadas no mês: {horas_trabalhadas}')
print(f'Valor recebido por hora: R$ {valor_ganho_por_hora}')
print(f'O seu salário no final do mês é: {salario}')