def resumo(valor=0, aumento=10, reducao=5):
    print('=' * 30)
    print('RESUMO DO VALOR'.center(30))
    print('=' * 30)
    print(f'Preço analisado: \t{moeda(valor)}')
    print(f'Dobro do preço: \t{dobro(valor, True)}')
    print(f'Metade do preço: \t{metade(valor, True)}')
    print(f'{aumento:2}% de aumento: \t{aumentar(valor, aumento, True)}')
    print(f'{reducao:2}% de redução: \t{diminuir(valor, reducao, True)}')
    print('=' * 30)


def moeda(valor=0, moeda='R$'):
    return f'{moeda}{valor:>.2f}'.replace('.', ',')


def aumentar(valor=0, taxa=0, formato=False):
    resultado = valor + valor * (taxa / 100)
    return resultado if formato is False else moeda(resultado)


def diminuir(valor=0, taxa=0, formato=False):
    resultado = valor - valor * (taxa / 100)
    return resultado if formato is False else moeda(resultado)


def dobro(valor=0, formato=False):
    resultado = valor * 2
    return resultado if formato is False else moeda(resultado)


def metade(valor=0, formato=False):
    resultado = valor / 2
    return resultado if formato is False else moeda(resultado)