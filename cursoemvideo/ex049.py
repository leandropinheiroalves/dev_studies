# EXERCÍCIO 49
"""
Refaça o exercício 009(tabuada), mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for.
"""

# PROGRAMA PRINCIPAL
numero = int(input('Digite um número: '))  # Recebe valor de numero
for i in range(1, 11):  # Loop de iteração do 1 ao 10
    print(f'{numero} x {i:2} = {numero * i}')  # Imprime a tabuada do numero
