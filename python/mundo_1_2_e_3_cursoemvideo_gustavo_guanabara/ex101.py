"""
Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro o ano de nascimento de uma pessoa,
retornando um valor literal indicando  se uma pessoa tem voto NEGADO, OPCIONAL ou OBRIGATÓRIO nas eleições.
"""


def voto(nascimento):  # Criando função voto com parâmetro nascimento
    from datetime import date  # Importa a função date do módulo datetime
    idade = date.today().year - nascimento  # Calcula a idade
    if 16 <= idade < 18 or idade > 65:  # Se a idade for menor que 18, maior igual a 16 ou maior que 65
        resultado = 'VOTO OPCIONAL.'  # Váriavel resultado recebe 'VOTO OPCIONAL.'
    elif idade >= 18:  # Mais se a idade a idade for maior igual 18
        resultado = 'VOTO  OBRIGATÓRIO.'  # Váriavel resultado recebe 'VOTO  OBRIGATÓRIO.'
    else:  # Senão
        resultado = 'NÃO VOTA.'  # Váriavel resultado recebe 'NÃO VOTA.'
    print('=' * 30)  # Imprime na tela espaçamento
    return print(f'Com {idade} anos: {resultado}')  # Retorna resultado da função voto


# Programa Principal
ano = int(input('Digite o ano do seu nascimento: '))  # Recebendo ano de nascimento do usuário
voto(ano)  # Executando função voto com valor ano
