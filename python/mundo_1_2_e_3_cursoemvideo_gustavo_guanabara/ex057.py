# EXERCÍCIO 57
"""
Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'.
Caso esteja errado, peça a digitação novamente até ter um valor correto.
"""

# PROGRAMA PRINCIPAL
sexo = str(input('Digite o seu sexo: [M/F] ')).strip()  # Recebe o sexo

while sexo[0] not in 'MmFf':  # Loop iterável ENQUANTO sexo não for masculino ou feminino
    sexo = str(input('Sexo inválido. Digite novamente o seu sexo: [M/F] ')).strip()  # Recebe o sexo

print(f'Sexo {sexo} registrado com sucesso.')  # Imprime o sexo
