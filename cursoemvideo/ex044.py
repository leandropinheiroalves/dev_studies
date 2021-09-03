# EXERCÍCIO 44
"""
Elabore um programa que calcule o valor a ser pago por um produto, considerando seu preço normal e tipo de pagamento:
    → À vista dinheiro/cheque: 10% de desconto
    → À vista no cartão: 5% de desconto
    → Em até 2x no cartão: preço normal
    → 3x ou mais no cartão: 20% de juros
"""

# PROGRAMA PRINCIPAL
produto = float(input('Digite o preço do produto: '))  # Recebe valor do produto
print('[1] À vista dinheiro/cheque \n[2] À vista cartão \n[3] 2x no cartão \n[4] 3x ou mais no cartão')
# ↑ Imprime as escolhas possíveis
escolha = int(input('Digite a opção escolhida: '))  # Recebe a escolha
if escolha == 1:  # SE a escolha for igual a 1
    desconto = produto * 0.1  # Calcula desconto de 10%
    print(f'Forma de pagamento escolhida: à vista dinheiro/cheque.')  # Imprime forma de pagamento
    print(f'Valor da compra: R${produto}')  # Imprime valor do produto
    print(f'Valor do desconto: R${desconto}')  # Imprime valor do desconto
    print(f'Valor a pagar: R${produto - desconto}')  # Imprime valor do produto com desconto
elif escolha == 2:  # MAIS SE a escolha for igual a 2
    desconto = produto * 0.05  # Calcula desconto de 5%
    print(f'Forma de pagamento escolhida: à vista cartão.')  # Imprime forma de pagamento
    print(f'Valor da compra: R${produto}')  # Imprime valor do produto
    print(f'Valor do desconto: R${desconto}')  # Imprime valor do desconto
    print(f'Valor a pagar: R${produto - desconto}')  # Imprime valor do produto com desconto
elif escolha == 3:  # MAIS SE a escolha for igual a 3
    parcela = produto / 2  # Calcula valor da parcela
    print(f'Forma de pagamento escolhida: 2x no cartão.')  # Imprime forma de pagamento
    print(f'Valor da compra: R${produto}')  # Imprime valor do produto
    print('Número de parcelas: 2')  # Imprime número de parcelas
    print(f'Valor de cada parcela: R${parcela}')  # Imprime valor das parcelas
elif escolha == 4:  # MAIS SE a escolha for igual a 4
    parcelas = int(input('Digite o número de vezes que deseja parcelar: '))  # Recebe n° de parcelas
    juros = produto * 1.2  # Adiciona 20% no valor do produto
    parcela = juros / parcelas  # Calcula o valor da parcela
    print(f'A forma de pagamento escolhida: 3x ou mais no cartão.')  # Imprime forma de pagamento
    print(f'Valor da compra: R${produto}')  # Imprime valor do produto
    print(f'Valor total com juros por parcelamento: R${juros}')  # Imprime valor do produto com juros
    print(f'Número de parcelas: {parcelas}')  # Imprime n° de parcelas
    print(f'Valor de cada parcela: R${parcela}')  # Imprime o valor de cada parcela
else:  # SENÃO
    print('Opção inválida. Tente novamente')  # Imprime mensagem de erro
