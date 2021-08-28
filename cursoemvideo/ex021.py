"""
Faça um programa em Python que abra e reproduza o áudio de um arquivo MP3.
"""

import pygame
pygame.init() # iniciar o pygame
pygame.mixer.music.load('ex021.mp3') # carrega o arquivo mp3
pygame.mixer.music.play() # toca o arquivo carregado
pygame.event.wait() # espera a musica acabar para encerrar o programa
