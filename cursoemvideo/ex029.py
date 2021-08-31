"""
Escreva um programa que leia a velocidade de um carro.
Se ele ultrapassar 80 Km/h, mostre uma mensagem dizendo que ele foi multado.
A multa vai custar R$7.00 por cada Km acima do limite.
"""
velocidade = float(input('Digite a velocidade atual do carro: '))  # Recebe uma velocidade em Km/h
if velocidade > 80:  # Se a velocidade ultrapassar o limite há uma multa
    print('Multado! Você ultrapassou o limite de velocidade.')  # Retorna mensagem da multa
    multa = (velocidade - 80) * 7  # Calcula o valor da multa
    print(f'O valor da multa é de R${multa:.2f}!')  # Retorna o valor da multa a ser pago
else: # Se a velocidade não ultrapassar o limite não há multa
    print('Sua velocidade está dentro dos limites.')  # Retorna mensagem padrão

# Solução Guanabara:
# velocidade = float(input('Qual é a velocidade atual do carro? '))
# if velocidade > 80:
#     print('MULTADO! Você excedeu o limite que é de 80Km/h')
#     multa = (velocidade-80) * 7
#     print('Você deve pagar uma multa de R${:.2f}'.format(multa))
# print('Tenha um bom dia! Dirija com segurança!')
