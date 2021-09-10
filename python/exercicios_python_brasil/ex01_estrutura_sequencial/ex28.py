"""O Hipermercado Tabajara está com uma promoção de carnes que é imperdível.
Confira:

                      Até 5 Kg           Acima de 5 Kg
File Duplo      R$ 4,90 por Kg          R$ 5,80 por Kg
Alcatra         R$ 5,90 por Kg          R$ 6,80 por Kg
Picanha         R$ 6,90 por Kg          R$ 7,80 por Kg

Para atender a todos os clientes, cada cliente poderá levar apenas um dos tipos
de carne da promoção, porém não há limites para a quantidade de carne por cliente.
Se compra for feita no cartão Tabajara o cliente receberá ainda um desconto de
5% sobre o total da compra. Escreva um programa que peça o tipo e a quantidade
de carne comprada pelo usuário e gere um cupom fiscal, contendo as informações
da compra: tipo e quantidade de carne, preço total, tipo de pagamento,
valor do desconto e valor a pagar.
"""

tipo_de_carne = str(input('Informe o tipo de carne desejado: [F-File Duplo / A-Alcatra / P-Picanha] ')).upper()
quantidade = valor_carne = tipo_pagamento = 0

if tipo_de_carne[0] in 'FAP':
    quantidade = float(input('Informe a quantidade em kg que deseja comprar de carne: '))
    tipo_pagamento = str(input('Informe o tipo de pagamento: [C-Cartão Tabajara / D-Dinheiro] ')).upper()
else:
    print('ERRO! Tipo de carne ínvalido. Tipos de carne disponíveis F-File Duplo, A-Alcatra e P-Picanha.')
    tipo_pagamento = ''

if tipo_de_carne[0] == 'F':
    carne = 'Filé Duplo'
    if quantidade > 5:
        valor_carne = 5.8
    else:
        valor_carne = 4.9
elif tipo_de_carne[0] == 'A':
    carne = 'Alcatra'
    if quantidade > 5:
        valor_carne = 6.8
    else:
        valor_carne = 5.9
elif tipo_de_carne[0] == 'P':
    carne = 'Picanha'
    if quantidade > 5:
        valor_carne = 7.8
    else:
        valor_carne = 6.9
else:
    tipo_pagamento = ' '

valor_total = valor_carne * quantidade

if tipo_pagamento[0] == 'C':
    desconto = valor_total * 0.05
    pagamento = 'Cartão Tabajara'
elif tipo_pagamento[0] == 'D':
    pagamento = 'Dinheiro'
    desconto = 0
else:
    print('ERRO! Tipo de pagamento ínvalido. [C-Cartão Tabajara / D - Dinheiro]')

if tipo_de_carne[0] in 'FAP' and quantidade != 0 and tipo_pagamento in 'CD':
    print(f'''
    ############ CUPOM FISCAL ############
    Tipo de carne      : {carne} 
    Quantidade         : {quantidade} kg
    Preço Total        : R$ {valor_total:.2f}
    Tipo de Pagamento  : {pagamento}
    Valor do Desconto  : R$ {desconto:.2f}
    Valor a Pagar      : R${(valor_total - desconto):.2f}
''')
