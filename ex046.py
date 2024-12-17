# ex046

'''Faça um programa que mostre na tela uma contagem regressiva para o estouro de fogos de artifício, indo de 10 até 0, com uma pausa de 1 segundo entre eles.'''

from emoji import emojize
from time import sleep as s
for c in range(10,0-1,-1):
    s(1)
    print(c)
print(emojize('BOOM! :fireworks::sparkle:'))
