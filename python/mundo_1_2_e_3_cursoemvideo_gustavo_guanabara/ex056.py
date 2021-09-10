# EXERCÍCIO 56
"""
Desenvolva um programa que leia o nome, idade e sexo  de 4 pessoas.
No final do programa, mostre:
    * A média de idade do grupo.
    * Qual é o nome do homem mais velho.
    * Quantas mulheres têm menos de 20 anos.
"""

# PROGRAMA PRINCIPAL
total_idades = idade_homem_mais_velho = mulheres_menores_20 = 0  # Criando variáveis com valor 0
nome_homem_mais_velho = ''  # Criando variável com valor vazio

for i in range(1, 5):  # Loop de iteração de 1 a 4
    print(f'----- {i}° PESSOA -----')  # Imprime ordem de cadastro da pessoa
    nome = str(input('Nome: ')).strip()  # Recebe o nome
    idade = int(input('Idade: '))  # Recebe a idade
    sexo = str(input('Sexo [M/F]: ')).strip().upper()  # Recebe o sexo e transforma em letra maiúscula
    total_idades += idade  # Incremento da variável total_idade

    if sexo == 'M' and idade_homem_mais_velho == 0:  # SE for o primeiro homem cadastrado
        idade_homem_mais_velho = idade  # Variável idade_homem_mais_velho recebe o valor de idade
        nome_homem_mais_velho = nome  # Variável nome_homem_mais_velho recebe o valor de nome

    if sexo == 'M' and idade > idade_homem_mais_velho:
    # ↑ SE for homem e tiver idade maior que a do homem mais velho
        idade_homem_mais_velho = idade  # Variável idade_homem_mais_velho recebe o valor de idade
        nome_homem_mais_velho = nome  # Variável nome_homem_mais_velho recebe o valor de nome

    if sexo == 'F' and idade < 20:  # SE a mulher tiver idade menor que 20
        mulheres_menores_20 += 1  # Incremento da variável mulheres_menores_20

media = total_idades / 4  # Calcula e recebe a média das idades

print(f'Média total de idades: {media:.1f} anos.')  # Imprime a média total
print(f'Homem mais velho: {nome_homem_mais_velho} com {idade_homem_mais_velho} anos.')
# ↑ Imprime o nome do homem mais velho e sua idade
print(f'Total de mulheres menores de 20 anos: {mulheres_menores_20}.')
# ↑ Imprime numero de mulheres menores que 20 anos
