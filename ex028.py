# ex028

'''Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador. 
O programa deverá escrever na tela se o usuário venceu ou perdeu.'''

import random
from time import sleep # Esse método da biblioteca time faz com que o computador demore alguns segundos para processar, --> melhor impressão de jogo !
print('-=-'*20,'\n',' '*15,'JOGO: ADIVINHE O NÚMERO\n','-=-'*20)
n=random.randint(0,5)
usuario=(input('Adivinhe um número de 0 a 5: '))
print('PROCESSANDO...')
sleep (3) # tempo : 3 segundos
if usuario==n:
    print('Parabéns! Você acertou')
else:
    print('Você errou! O número correto era {} e não {}\nTente novamente'.format(n,usuario))

# Lembrete que :< alinha a esquerda e :> alinha a direita
# :^ alinha no centro
