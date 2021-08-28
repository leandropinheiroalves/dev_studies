"""
Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
    * À vista dinheiro/cheque: 10% de desconto
    * À vista no cartão: 5% de desconto
    * Em até 2x no cartão: preço normal
    * 3x ou mais no cartão: 20% de juros
"""
produto = 4000
print('''[1] À vista dinheiro ou cheque
[2] À vista no cartão
[3] 2x no cartão
[4] 3x ou mais no cartão
''')
escolha = int(input('''[1] À vista dinheiro ou cheque
[2] À vista no cartão
[3] 2x no cartão
[4] 3x ou mais no cartão
Digite a opção escolhida: '''))
if escolha == 1:
    desconto = produto * 0.1
    print(f'''A forma de pagamento escolhida foi à vista no dinheiro ou cheque.
Valor da compra: R${produto}
Valor do desconto: R${desconto}
Valor a pagar: R${produto - desconto}''')
elif escolha == 2:
    desconto = produto * 0.05
    print(f'''A forma de pagamento escolhida foi à vista no cartão.
Valor da compra: R${produto}
Valor do desconto: R${desconto}
Valor a pagar: R${produto - desconto}''')
elif escolha == 3:
    parcela = produto / 2
    print(f'''A forma de pagamento escolhida foi parcelamento em 2 vezes no cartão.
Valor da compra: R${produto}
Número de parcelas: 2
Valor de cada parcela: R${parcela}''')
elif escolha == 4:
    parcelas = int(input('Digite o número de vezes que deseja parcelar: '))
    parcela = (produto * 1.2) / parcelas
    print(f'''A forma de pagamento escolhida foi parcelamento em 3 vezes ou mais no cartão.
Valor da compra: R${produto}
Valor total com juros por parcelamento: R${produto * 1.2}
Número de parcelas: {parcelas}
Valor de cada parcela: R${parcela}''')
else:
    print('Opção inválida. Tente novamente')