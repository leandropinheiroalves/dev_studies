"""
Desenvolva um programa que leia o nome, idade e sexo  de 4 pessoas.
No final do programa, mostre:
    * A média de idade do grupo.
    * Qual é o nome do homem mais velho.
    * Quantas mulheres têm menos de 20 anos.
"""
total_idades = idade_homem_mais_velho = mulheres_menores_20 = 0
nome_homem_mais_velho = ''
for i in range(1, 5):
    print(f'----- {i}° PESSOA -----')
    nome = str(input('Nome: ')).strip().capitalize()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip().upper()
    total_idades += idade
    if sexo == 'M' and idade_homem_mais_velho == 0:
        idade_homem_mais_velho = idade
        nome_homem_mais_velho = nome
    if sexo == 'M' and idade > idade_homem_mais_velho:
        idade_homem_mais_velho = idade
        nome_homem_mais_velho = nome
    if sexo == 'F' and idade < 20:
        mulheres_menores_20 += 1
media = total_idades / 4
print(f'Média total de idades: {media:.1f} anos.')
print(f'Homem mais velho: {nome_homem_mais_velho} com {idade_homem_mais_velho} anos.')
print(f'Total de mulheres menores de 20 anos: {mulheres_menores_20}.')
