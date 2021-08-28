"""
Escreva um programa que leia a velocidade de um carro.
Se ele ultrapassar 80 Km/h, mostre uma mensagem dizendo que ele foi multado.
A multa vai custar R$7.00 por cada Km acima do limite.
"""
velocidade = float(input('Digite a velocidade atual do carro: '))
if velocidade > 80:
    print('Você foi multado por ultrapassar o limite de velocidade que é 80 Km/h')
    multa = (velocidade - 80) * 7
    print(f'O valor da multa é de R${multa:.2f}!')
else:
    print('Sua velocidade está dentro dos limites.')

# Solução Guanabara:
# velocidade = float(input('Qual é a velocidade atual do carro? '))
# if velocidade > 80:
#     print('MULTADO! Você excedeu o limite que é de 80Km/h')
#     multa = (velocidade-80) * 7
#     print('Você deve pagar uma multa de R${:.2f}'.format(multa))
# print('Tenha um bom dia! Dirija com segurança!')
