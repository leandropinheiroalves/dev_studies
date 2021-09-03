# EXERCÍCIO 36
"""
Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
O programa vai perguntar o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário ou então o empréstimo será negado.
"""

# PROGRAMA PRINCIPAL
casa = float(input('Digite o valor da casa: '))  # Recebendo valor da casa
salario = float(input('Digite o valor do seu salário: '))  # Recebendo salário
anos = int(input('Digite em quantos anos deseja pagar: '))  # Recebendo anos
mensalidade = casa / (anos * 12)  # Variável mensalidade recebendo valor do cálculo da mensalidade
if mensalidade > (salario * 0.3):  # SE a mensalidade for maior que 30% do salário
    print(f'Empréstimo Negado! A mensaliade é R${mensalidade:.2f} e ultrapassa 30% do seu salário!')
    # ↑ Imprime mensagem de empréstimo negado
elif 0 < mensalidade < (salario * 0.3):  # MAIS SE mensalidade maior que 0 e menor que 30% do salário
    print(f'Empréstimo Aprovado! O valor da sua mensalidade é de R${mensalidade:.2f}.')
    # ↑ Imprime mensagem de empréstimo aprovado
else:  # SENÃO
    print('Ouve algum erro, tente novamente.')  # Imprime mensagem de erro
