#ex021

'''Faça um programa em Python que abra e reproduza o áudio de um arquivo MP3.'''

import pygame
pygame.init()
pygame.mixer.music.load('Paragraphs.mp3')
pygame.mixer.music.play()
input(f'{'\033[36m'}enter to exit')
