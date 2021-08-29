"""
Crie um programa que leia o nome e o preço de vários produtos.
O programa deverá perguntar se o usuário vai continuar.
No final, mostre:
    * Qual é o total gasto na compra.
    * Quantos produtos custam mais de R$1000.
    * Qual é o nome do produto mais barato.
"""
total = barato = caro = 0
nome_barato = ' '
while True:
    produto = str(input('Digite o nome do produto: ')).strip()
    valor = float(input('Digite o valor do produto: '))
    escolha = ' '
    if total == 0:
        total = barato = valor
        nome_barato = produto
    else:
        total += valor
        if valor < barato:
            barato = valor
            nome_barato = produto
    if valor > 1000:
        caro += 1
    while escolha not in 'NS':
        escolha = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    if escolha == 'N':
        break
print(f'''Preço total da compra: R${total:.2f}
Produtos acima de R$1000: {caro}
Produto mais barato: {nome_barato} custou R${barato:.2f}
''')
