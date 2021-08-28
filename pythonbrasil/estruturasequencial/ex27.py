"""Uma fruteira está vendendo frutas com a seguinte tabela de preços:

                      Até 5 Kg           Acima de 5 Kg
Morango         R$ 2,50 por Kg          R$ 2,20 por Kg
Maçã            R$ 1,80 por Kg          R$ 1,50 por Kg

Se o cliente comprar mais de 8 Kg em frutas ou o valor total da compra
ultrapassar R$ 25,00, receberá ainda um desconto de 10% sobre este total.

Escreva um algoritmo para ler a quantidade (em Kg) de morangos e a
quantidade (em Kg) de maças adquiridas e escreva o valor a ser pago pelo cliente.
"""

morangos = float(input('Digite a quantidade em Kg que deseja comprar de MORANGOS: '))
macas = float(input('Digite a quantidade em Kg que deseja comprar de MAÇAS: '))

if morangos > 5:
    valor_morango = 2.2
else:
    valor_morango = 2.5

if macas > 5:
    valor_macas = 1.5
else:
    valor_macas = 1.8

total_morango = morangos * valor_morango
total_macas = macas * valor_macas
total_compra = total_macas + total_morango

if (morangos + macas) > 8 or total_compra > 25:
    print(f'Parabéns, você ganhou 10% de desconto, valor a ser pago sem desconto: R$ {total_compra:.2f}')
    total_compra *= 0.9
    print(f'Você comprou {morangos + macas} Kg de frutas, o valor a ser pago com desconto: R$ {total_compra:.2f}')
else:
    print(f'Você comprou {morangos + macas} Kg de frutas, o valor a ser pago é: R$ {total_compra:.2f}')
