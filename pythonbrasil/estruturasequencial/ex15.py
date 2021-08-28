"""Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas
no mês. Calcule e mostre o total do seu salário no referido mês, sabendo-se que
são descontados 11% para o Imposto de Renda, 8% para o INSS e 5% para o sindicato,
faça um programa que nos dê:
a. salário bruto.
b. quanto pagou ao INSS.
c. quanto pagou ao sindicato.
d. o salário líquido.
e. calcule os descontos e o salário líquido, conforme a tabela abaixo:
    + Salário Bruto : R$
    - IR (11%) : R$
    - INSS (8%) : R$
    - Sindicato ( 5%) : R$
    = Salário Liquido : R$
Obs.: Salário Bruto - Descontos = Salário Líquido."""

valor_ganho_por_hora = float(input('Informe o valor ganho por hora trabalhada: '))
horas_trabalhadas_mes = float(input('Informe o numero de horas trabalhadas no mês: '))

salario_bruto = valor_ganho_por_hora * horas_trabalhadas_mes
ir = salario_bruto * 0.11
inss = salario_bruto * 0.08
sindicato = salario_bruto * 0.05
salario_liquido = salario_bruto - (ir + inss + sindicato)

print(f'''Horas trabalhadas no mês: {horas_trabalhadas_mes} horas 
Valor recebido por hora: R$ {valor_ganho_por_hora}
    + Salário Bruto     : R$ {salario_bruto}
    - IR (11%)          : R$ {ir}
    - INSS (8%)         : R$ {inss}
    - Sindicato ( 5%)   : R$ {sindicato}
    = Salário Liquido   : R$ {salario_liquido}
''')
