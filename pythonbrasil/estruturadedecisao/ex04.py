"""Faça um Programa que verifique se uma letra digitada é vogal ou consoante."""

letra = str(input('Digite uma letra: ')).upper()

if letra[0] in 'AEIOU':
    print('A letra digitada é uma VOGAL.')
else:
    print('A letra digita é uma CONSOANTE.')