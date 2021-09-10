"""Faça um programa para o cálculo de uma folha de pagamento, sabendo que os
descontos são do Imposto de Renda, que depende do salário bruto
(conforme tabela abaixo) e 3% para o Sindicato e que o
FGTS corresponde a 11% do Salário Bruto, mas não é descontado
(é a empresa que deposita).
O Salário Líquido corresponde ao Salário Bruto menos os descontos. O programa
deverá pedir ao usuário o valor da sua hora e a quantidade de horas trabalhadas no mês.
Desconto do IR:
    * Salário Bruto até 900 (inclusive) - isento
    * Salário Bruto até 1500 (inclusive) - desconto de 5%
    * Salário Bruto até 2500 (inclusive) - desconto de 10%
    * Salário Bruto acima de 2500 - desconto de 20% Imprima na tela as informações,
    dispostas conforme o exemplo abaixo.
    No exemplo o valor da hora é 5 e a quantidade de hora é 220.
        Salário Bruto: (5 * 220)        : R$ 1100,00
        (-) IR (5%)                     : R$   55,00
        (-) INSS ( 10%)                 : R$  110,00
        FGTS (11%)                      : R$  121,00
        Total de descontos              : R$  165,00
        Salário Liquido                 : R$  935,00"""

horas_trabalhadas_no_mes = 220
valor_recebido_por_hora = 2
salario_bruto = horas_trabalhadas_no_mes * valor_recebido_por_hora
sindicato = salario_bruto * 0.03
fgts = salario_bruto * 0.11

if salario_bruto <= 900:
    ir = 0
elif salario_bruto <= 1500:
    ir = 5
elif salario_bruto <= 2500:
    ir = 10
elif salario_bruto > 2500:
    ir = 20

valor_ir = salario_bruto * (ir / 100)
descontos = sindicato + ir
salario_liquido = salario_bruto - descontos

print(f'''
        Salário Bruto: (5 * 220)        : R$ {salario_bruto}
        (-) IR ({ir}%)                    : R$ {valor_ir} 
        (-) Sindicato (3%)              : R$ {sindicato}
        FGTS (11%)                      : R$ {fgts}
        Total de descontos              : R$ {descontos}
        Salário Liquido                 : R$ {salario_liquido}
''')