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