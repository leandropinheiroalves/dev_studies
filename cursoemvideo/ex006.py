"""
Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.
"""
numero = int(input('Digite um número: '))
dobro = numero * 2
triplo = numero * 3
raiz = numero ** (1/2)
print(f'O dobro do número informado é \033[2;36m{numero}\033[m, o triplo é \033[2;40m{triplo}\033[m e a raiz quadrada é \033[3;32m{raiz:.2f}\033[m')

