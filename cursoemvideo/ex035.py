"""
Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.
"""
reta_1 = float(input('Digite o primeiro valor: '))
reta_2 = float(input('Digite o segundo valor: '))
reta_3 = float(input('Digite o terceiro valor: '))
if reta_1 > (reta_2 + reta_3) or reta_2 > (reta_1 + reta_3) or reta_3 > (reta_2 + reta_1):
    print('Os valores informados não formam um triângulo.')
else:
    print('Os valores informados formam um triângulo.')

# # Solução Guanabara
# print('-='*20)
# print('Analisador de Triângulos')
# print('-+'*20)
# r1 = float(input('Primeiro segmento: '))
# r2 = float(input('Segundo segmento: '))
# r3 = float(input('Terceiro segmento: '))
# if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
#     print('Os segmentos acima PODEM FORMAR triângulo!')
# else:
#     print('Os segmentos acima NÃO PODEM FORMAR triângulo.')
