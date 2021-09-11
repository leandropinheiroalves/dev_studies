def contar_caracteres(s):
    """Função que conta os caracteres de uma string

    Ex:

    >>> contar_caracteres('renzo')
    {'e': 1, 'n': 1, 'o': 1, 'r': 1, 'z': 1}
    >>> contar_caracteres('banana')
    {'a': 3, 'b': 1, 'n': 2}

    :param s: string a ser contada
    """


    resultado = {}

    for caracter in s:  # para cada letra depois da primeira
        resultado[caracter] = resultado.get(caracter, 0) + 1

    return resultado

if __name__ == '__main__':  # só executa no módulo
    print(contar_caracteres('renzo'))  # executa função contar_caracteres
    print()  # pula linha
    print(contar_caracteres('banana'))  # executa função contar_caracteres
