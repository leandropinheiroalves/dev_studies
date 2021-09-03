def leiadinheiro(mensagem):
    valido = False
    while not valido:
        entrada = str(input(mensagem)).replace(',', '.').strip()
        if entrada.isalpha() or entrada == '':
            print(f'\033[31mERRO: "{entrada}" é um preço inválido!\033[m')
        else:
            valido = True
            return float(entrada)


def leiaInt(mensagem):
    a = input(mensagem)
    while not a.isnumeric():
        print('\033[31mERRO! Digite um número inteiro válido.\033[m')
        a = input(mensagem)
    return a
