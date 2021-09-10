# Calculadora em Python

# Desenvolva uma calculadora em Python com tudo que você aprendeu nos capítulos 2 e 3. 
# A solução será apresentada no próximo capítulo!
# Assista o vídeo com a execução do programa!
print("\n******************* Python Calculator *******************")
print('[1] - Soma \n[2] - Subtração \n[3] - Multiplicação \n[4] - Divisão')

escolha = int(input('Escolha uma das operações: '))

if escolha > 4 or escolha < 1:
    print('Erro! Operação escolhida é inválida.')

else:
    numero_1 = int(input('Digite o primeiro número: '))
    numero_2 = int(input('Digite o segundo número: '))

    if escolha == 1:
        soma = numero_1 + numero_2
        print(f'{numero_1} + {numero_2} = {soma}')

    elif escolha == 2:
        subracao = numero_1 - numero_2
        print(f'{numero_1} - {numero_2} = {subracao}')

    elif escolha == 3:
        multiplicacao = numero_1 * numero_2
        print(f'{numero_1} * {numero_2} = {multiplicacao}')
        
    elif escolha == 4:
        divisao = numero_1 * numero_2
        print(f'{numero_1} / {numero_2} = {divisao}')
