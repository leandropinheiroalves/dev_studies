def moeda(valor=0, moeda='R$'):
    return f'{moeda}{valor:>.2f}'.replace('.', ',')


def aumentar(valor=0, taxa=0):
    resultado = valor + valor * (taxa / 100)
    return resultado


def diminuir(valor=0, taxa=0):
    resultado = valor - valor * (taxa / 100)
    return resultado


def dobro(valor=0):
    resultado = valor * 2
    return resultado


def metade(valor=0):
    resultado = valor / 2
    return resultado
