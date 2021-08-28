"""Faça um programa que leia um nome de usuário e a sua senha e
não aceite a senha igual ao nome do usuário, mostrando uma mensagem de erro
e voltando a pedir as informações.
"""

usuario = str(input('Digite um nome de usuário: '))
senha = str(input('Digite uma senha: '))

while usuario == senha:
    print('ERRO! O nome de usuário e senha precisam ser diferentes!')
    usuario = str(input('Digite um nome de usuário: '))
    senha = str(input('Digite uma senha: '))

print(f'''\nNome de usuário: {usuario} / Senha: {senha}''')
