"""Faça um programa que pergunte o preço de três produtos e informe qual
produto você deve comprar, sabendo que a decisão é sempre pelo mais barato."""

produto_1 = int(input('Digite o valor do primeiro produto: '))
produto_2 = int(input('Digite o valor do segundo produto: '))
produto_3 = int(input('Digite o valor do terceiro produto: '))

if produto_1 < produto_2 and produto_1 < produto_3:
    print(f'O produto mais barato é o primeiro produto custando: {produto_1}')
elif produto_2 < produto_1 and produto_2 < produto_3:
    print(f'O produto mais barato é o segundo produto custando: {produto_2}')
elif produto_3 < produto_2 and produto_3 < produto_1:
    print(f'O produto mais barato é o terceiro produto custando: {produto_3}')
else:
    print('Ouve algum erro, tente novamente.')