"""Faça um Programa que peça um número correspondente a um determinado ano e
em seguida informe se este ano é ou não bissexto."""

ano = int(input('Digite um ano para saber se ele é Bissexto: '))

if ano % 4 == 0: # se a divisão do ano por 4 for exata, pode ser bissexto
    if ano % 100 == 0: # se a divisão do ano por 100 for exata, não é bissexto, a menos que a divisão por 400 seja exata.
        if ano % 400 == 0:
            resultado = 'é Bissexto'
        else:
            resultado = 'não é Bissexto'
    else:
        resultado = 'é Bissexto'
else:
    resultado = 'não é Bissexto'

print(f'O ano {ano} {resultado}')




