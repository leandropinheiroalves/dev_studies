"""
Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-os (com idade) em um dicionário
se por acaso a CTPS for diferente de ZERO, o dicionário receberá também o ano de contratação e o salário.
Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.
A aposentadoria no exercício se dá com 35 anos de contribuição.
"""
from datetime import date  # Importando função date do módulo datetime
cadastro = dict()  # Criando dicionário
cadastro['nome'] = str(input('Digite o nome: '))  # Recebendo valor e adicionando na chave 'nome'
nascimento = int(input('Digite o ano de nascimento: '))  # Váriavel Recebendo valor do usuário
cadastro['ctps'] = int(input('Digite o número da Carteira de Trabalho (0 não tem): '))
# Recebendo valor e adicionando na chave 'ctps'

cadastro['idade'] = date.today().year - nascimento  # Calculando o valor e adicionando na chave 'idade'
if cadastro['ctps'] != 0:  # Se o valor da chave 'ctps' for diferente de zero
    cadastro['contratação'] = int(input('Digite o ano de contratação: '))
    # Recebendo valor e adicionando na chave 'contratação'

    cadastro['aposentadoria'] = (cadastro['idade'] + 35) - (date.today().year - cadastro['contratação'])
    # Calculando o valor e adicionando na chave 'aposentadoria'

    cadastro['salário'] = float(input('Digite o salário: R$'))  # Recebendo valor e adicionando na chave 'salário'
    print()  # Quebra de  linha
    for k, v in cadastro.items():  # Loop de iteração para cada item do dicionário cadastro
        print(f'{k.capitalize():<18}: {v:<15}')  # Retornando chave e valor
else:
    print()  # Quebra de  linha
    for k, v in cadastro.items():  # Loop de iteração para cada item do dicionário cadastro
        print(f'{k.capitalize():<18}: {v:<15}')  # Retornando chave e valor