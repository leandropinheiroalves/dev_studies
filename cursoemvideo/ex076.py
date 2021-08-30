"""
Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequência.
No final, mostre uma listagem de preços, organizando os dados em forma tabular.
"""
listagem = ('Lápis', 1.75,
            'Borracha', 2,
            'Caderno', 15.9,
            'Estojo', 25,
            'Transferidor', 4.2,
            'Compasso', 9.99,
            'Mochila', 120.32,
            'Canetas', 22.3,
            'Livro', 34.9)
print('=' * 30)
print('{:^30}  '.format('LISTAGEM DE PREÇOS'))
print('=' * 30)
for item in range(0, len(listagem), 2):
    print('{:.<20}R${:>8.2f}'.format(listagem[item], listagem[item+1]))
print('=' * 30)
