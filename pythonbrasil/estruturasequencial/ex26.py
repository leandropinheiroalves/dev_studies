"""Um posto está vendendo combustíveis com a seguinte tabela de descontos:
    * Álcool:
        * até 20 litros, desconto de 3% por litro
        * acima de 20 litros, desconto de 5% por litro
    * Gasolina:
        * até 20 litros, desconto de 4% por litro
        * acima de 20 litros, desconto de 6% por litro
Escreva um algoritmo que leia o número de litros vendidos, o tipo de
combustível (codificado da seguinte forma: A-álcool, G-gasolina),
calcule e imprima o valor a ser pago pelo cliente sabendo-se que o preço do litro
da gasolina é R$ 2,50 o preço do litro do álcool é R$ 1,90."""

litros_vendidos = float(input('Digite o total de litros que deseja comprar: '))
tipo_de_combustivel = str(input('Digite o tipo de combustível: [A-Álcool / G-Gasolina] ')).upper()
preco_gasolina = 2.5
preco_alcool = 1.9

if tipo_de_combustivel[0] == 'A':
    combustivel = 'Álcool'
    if litros_vendidos > 20:
        valor_a_ser_pago = (preco_alcool * litros_vendidos) * 0.95
    else:
        valor_a_ser_pago = (preco_alcool * litros_vendidos) * 0.97
elif tipo_de_combustivel[0] == 'G':
    combustivel = 'Gasolina'
    if litros_vendidos > 20:
        valor_a_ser_pago = (preco_gasolina * litros_vendidos) * 0.94
    else:
        valor_a_ser_pago = (preco_gasolina * litros_vendidos) * 0.96

if tipo_de_combustivel[0] in 'AG':
    print(f'''Tipo de combustível escolhido : {combustivel}
Quantidade de combustível     : {litros_vendidos} litros
Valor total a ser pago        : R$ {valor_a_ser_pago:.2f}
''')
else:
    print('ERRO! Tipo de combustível ínvalido.')