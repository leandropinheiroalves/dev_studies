"""Faça um Programa que verifique se uma letra digitada é "F" ou "M".
Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido."""

letra = str(input('Digite F ou M: ')).upper()

if letra[0] == 'F':
    print('Feminino')
elif letra[0] == 'M':
    print('Masculino')
else:
    print('Sexo Inválido')