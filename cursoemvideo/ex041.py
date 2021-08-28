"""
A confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categora, de acordo com a idade:
    * Até 9 anos: MIRIM
    * Até 14 anos: INFANTIL
    * Até 19 anos: JUNIOR
    * Até 20 anos: SÊNIOR
    * Acima: MASTER
"""
from datetime import date
ano = 2000
atual = date.today().year
idade = atual - ano
if idade <= 9:
    categoria = 'MIRIM'
elif idade <= 14:
    categoria = 'INFANTIL'
elif idade <= 19:
    categoria = 'JUNIOR'
elif idade <= 20:
    categoria = 'SENIOR'
elif idade > 20:
    categoria = 'MASTER'

print(f'''O atleta tem {idade} anos e faz parte da Categoria {categoria}''')
