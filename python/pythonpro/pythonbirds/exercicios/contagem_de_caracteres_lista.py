def contar_caracteres(s):
    """Função que conta os caracteres de uma string

    Ex:

    >>> contar_caracteres('renzo')
    e: 1
    n: 1
    o: 1
    r: 1
    z: 1
    >>> contar_caracteres('banana')
    a: 3
    b: 1
    n: 2

    :param s: string a ser contada
    """
    caracteres_ordenados = sorted(s)  # ordenando a palavra a ser contada

    caracter_anterior = caracteres_ordenados[0]  # variavel com o valor da primeira letra
    contagem = 1  # contagem começa em 1

    for caracter in caracteres_ordenados[1:]:  # para cada letra depois da primeira
        if caracter == caracter_anterior:  # se a letra for igual a anterior
            contagem += 1  # incrementa a contagem
        else:  # senão
            print(f'{caracter_anterior}: {contagem}')  # imprime a letra e a contagem
            caracter_anterior = caracter  # o caracter anterior se torna a letra
            contagem = 1  # a contagem volta pra 1

    print(f'{caracter_anterior}: {contagem}')  # imprime a ultima letra e a contagem dela fora do for

if __name__ == '__main__':  # só executa no módulo
    contar_caracteres('renzo')  # executa função contar_caracteres
    print()  # pula linha
    contar_caracteres('banana')  # executa função contar_caracteres
