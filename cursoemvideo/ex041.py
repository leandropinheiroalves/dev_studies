# EXERCÍCIO 41
"""
A confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categora, de acordo com a idade:
    → Até 9 anos: MIRIM
    → Até 14 anos: INFANTIL
    → Até 19 anos: JUNIOR
    → Até 20 anos: SÊNIOR
    → Acima: MASTER
"""

# PROGRAMA PRINCIPAL
from datetime import date  # Importando função date do módulo datetime
ano = int(input('Digite o ano de nascimento do atleta: '))  # Recebendo ano
atual = date.today().year  # Calcula ano atual
idade = atual - ano  # Calcula idade
if idade <= 9:  # SE idade menor ou igual 9
    categoria = 'MIRIM'  # Variável categoria recebe 'MIRIM'
elif idade <= 14:  # MAIS SE idade menor ou igual 14
    categoria = 'INFANTIL'  # Variável categoria recebe 'INFANTIL'
elif idade <= 19:  # MAIS SE idade menor ou igual 19
    categoria = 'JUNIOR'  # Variável categoria recebe 'JUNIOR'
elif idade <= 20:  # MAIS SE idade menor ou igual 20
    categoria = 'SENIOR'  # Variável categoria recebe 'SENIOR'
elif idade > 20:  # MAIS SE idade maior que 20
    categoria = 'MASTER'  # Variável categoria recebe 'MASTER'
else:  # SENÃO
    categoria = ''  # Variável categoria se torna vazia
if idade >= 0:  # SE a idade for maior ou igual a 0
    print(f'O atleta tem {idade} anos e é da categoria {categoria}.')  # Imprime idade e categoria
else:  # SENÃO
    print(f'ERRO! O ano informado é de um atleta que ainda não nasceu.')  # Imprime erro
