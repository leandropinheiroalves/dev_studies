"""Faça um programa que peça o tamanho de um arquivo para download (em MB)
e a velocidade de um link de Internet (em Mbps), calcule e informe o tempo
aproximado de download do arquivo usando este link (em minutos)."""

tamanho_arquivo = 255
velocidade_de_download = 10
tempo_estimado = tamanho_arquivo / (velocidade_de_download/8)

print(f'Tamanho do arquivo      : {tamanho_arquivo} MB')
print(f'Velocidade de download  : {velocidade_de_download} Mbps')
print(f'O seu download será concluído em aproximadamente: {tempo_estimado:.2f} segundos.')