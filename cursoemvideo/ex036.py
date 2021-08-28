"""
Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
O programa vai perguntar o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário ou então o empréstimo será negado.
"""
casa = float(input('Digite o valor da casa: '))
salario = float(input('Digite o valor do seu salário: '))
anos = int(input('Digite em quantos anos deseja pagar: '))
mensalidade = casa / (anos * 12)
if mensalidade > (salario * 0.3):
    print(f'Empréstimo Negado! A mensaliade é R${mensalidade:.2f} e ultrapassa 30% do seu salário!')
elif 0 < mensalidade < (salario * 0.3):
    print(f'Empréstimo Aprovado! O valor da sua mensalidade é de R${mensalidade:.2f}.')
else:
    print('Ouve algum erro, tente novamente.')
