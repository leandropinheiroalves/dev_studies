"""
Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'.
Caso esteja errado, peça a digitação novamente até ter um valor correto.
"""
sexo = str(input('Digite o seu sexo: [M/F] ')).strip()
while sexo[0] not in 'MmFf':
    sexo = str(input('Sexo inválido. Digite novamente o seu sexo: [M/F] ')).strip()
print(f'Sexo {sexo} registrado com sucesso.')
