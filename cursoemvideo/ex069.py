"""
Crie um programa que leia a idade e o sexo de várias pessoas.
A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar.
No final, mostre:
    * quantas pessoas tem mais de 18 anos.
    * quantos homens foram cadastrados.
    * quantas mulheres tem menos de 20 anos.
"""
maiores = homens = mulheres = 0
while True:
    idade = int(input('Digite a idade: '))
    sexo = escolha = ' '
    while sexo not in 'MF':
        sexo = str(input('Digite o sexo [F/M]: ')).strip().upper()[0]
    if idade > 18:
        maiores += 1
    if sexo == 'M':
        homens += 1
    if sexo == 'F' and idade < 20:
        mulheres += 1
    while escolha not in 'SN':
        escolha = str(input('Deseja Continuar? [S/N] ')).strip().upper()[0]
    if escolha == 'N':
        break
print(f'''Maiores de 18: {maiores}
Homens: {homens}
Mulheres menores de 20: {mulheres}''')
