# EXERCÍCIO 31
"""
Desenvolva um programa que pergunte a distância de uma viagem em Km.
Calcule o preço da passagem, cobrando R$0.50 por Km para viagens de até 200Km e R$0.45 para viagens mais longas.
"""

# PROGRAMA PRINCIPAL
distancia = float(input('Digite a distância da sua viagem: '))  # Recebendo distância da viagem
if distancia <= 200:  # SE a distância for menor ou igual a 200
    taxa = 0.50  # Taxa de R$0.50
else:  # SENÃO
    taxa = 0.45  # Taxa de R$0.45
passagem = taxa * distancia  # Calculando valor da passagem
print(f'O preço da passagem de uma viagem de {distancia:.1f} Km é de R${passagem:.2f}.')
# ↑ Imprimindo resultado na tela

# SOLUÇÃO GUANABARA
# distância = float(input('Qual é a distância da sua viagem? '))
# # preço = distância * 0.50 if distância <= 200 else distância * 0.45 # forma simplificada
# if distância <= 200:
#     preço = distância * 0.50
# else:
#     preço = distância * 0.45
# print('E o preço da sua passagem será de R${:.2f}'.format(preço))
